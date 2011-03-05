import logging
import threading
import json
import os
import socket
import datetime

import settings
import pika

class QueueLoggingHandler(logging.Handler):
    """
    A simple logging handler to submit logging records to an AMQP queue.
    """
    
    def __init__(self, level=logging.NOTSET):
        logging.Handler.__init__(self, level=level)
        self.__queueHost = settings.config['logging.queue_host']
        self.__queueName = settings.config['logging.queue_name']
        self.__producer = settings.config['logging.producer']
        
    def emit(self, record):
        connection = None
        channel = None
        try:
            connection = self.fresh_connection()
            channel = connection.channel()
            channel.queue_declare(
                queue=self.__queueName,
                durable=True,
                exclusive=False,
                auto_delete=False)
            
            channel.basic_publish(
                exchange='',
                routing_key=self.__queueName,
                body=json.dumps({
                    'producer': self.__producer,
                    'host': socket.gethostname(),
                    'pid': os.getpid(),
                    'level_name': record.levelname,
                    'level_num': record.levelno,
                    'message': self.__format_message(record.getMessage())
                }),
                properties=pika.BasicProperties(
                    content_type='application/json',
                    # deliver_mode=2 <= persistent
                    delivery_mode=2))
        except Exception as e:
            print('Encountered an exception: ' + str(e))
            print(type(e))
        finally:
            if not channel is None:
                channel.close()
                
            if not connection is None:
                connection.close()
                
    def __format_message(self, message):
        now = datetime.datetime.now()
        #return ('[%02d/%s/%04d:%02d:%02d:%02d]' %
        #        (now.day, month, now.year, now.hour, now.minute, now.second))
        return '[{1:04}-{2:02}-{3:02} {4:02}:{5:02}:{6:02}] {0}'.format(message, now.year, now.month, now.day, now.hour, now.minute, now.second)
            
    def fresh_connection(self):
        return pika.AsyncoreConnection(
            parameters=pika.ConnectionParameters(host=self.__queueHost))
        