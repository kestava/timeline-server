import logging
import threading
import json
import os
import socket

import settings
import pika

class QueueLoggingHandler(logging.Handler):
    """
    A simple logging handler to submit logging records to an AMQP queue.
    """
    
    def __init__(self, level=logging.NOTSET):
        logging.Handler.__init__(self, level=level)
        
        try:
            self.__open_channel()
        except Exception, e:
            print(e)
            
    def __open_channel(self):
        params = pika.ConnectionParameters(
            host=settings.config['logging.host'])
        
        reconnStrategy = pika.SimpleReconnectionStrategy()
        self.__connection = pika.AsyncoreConnection(
            parameters=params,
            reconnection_strategy=reconnStrategy)
        self.__channel = self.__connection.channel()
        
        # Set up the queue to which we'll be sending messages
        self.__channel.queue_declare(
            queue=settings.config['logging.queue_name'],
            durable=True,
            exclusive=False,
            auto_delete=False)
    
    def close(self):
        logging.Handler.close(self)
        self.__channel.close()
        self.__connection.close()
        
    def emit(self, record):
        self.__channel.basic_publish(
            exchange='',
            routing_key=settings.config['logging.queue_name'],
            body=json.dumps({
                'producer': settings.config['logging.producer'],
                'host': socket.gethostname(),
                'pid': os.getpid(),
                'level_name': record.levelname,
                'level_num': record.levelno,
                'message': record.getMessage()
            }))