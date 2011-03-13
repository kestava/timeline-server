"""
This is the database module.
"""
import pprint
import logging

import cherrypy

import connection

class Database(object):
    
    @classmethod
    def __get_connection(cls):
        a = cherrypy.request.app.config
        #pprint(a)
        return connection.Connection()

    @classmethod
    def get_messages(cls, max, since=None):
        """
        Return a set of messages.
        
        Keyword arguments:
        max -- The maximum number of messages to return
        since -- A timestamp used to determine the first message of the set
        """
        logging.getLogger('app').debug('Inside Database.get_last_n_messages')
    
        with cls.__get_connection() as cnx:
            data = cnx.fetchall('select * from messages')
            
        pprint.pprint(data)
    
        return "'yeah!'"
