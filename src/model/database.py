import pprint
import logging

import cherrypy
from psycopg2 import connect
from psycopg2.extras import DictCursor

class Database(object):

    @classmethod
    def __get_connection(cls):
        a = cherrypy.request.app.config
        #pprint(a)
        return Connection()

    @classmethod
    def get_last_n_messages(cls, n):
        logging.getLogger('app').debug('Inside Database.get_last_n_messages')
    
        with cls.__get_connection() as connection:
            pass
    
        return "'yeah!'"
        
class Connection(object):
    
    def __enter__(self):
        pass
    
    def __exit__(self, type, value, traceback):
        pass
        