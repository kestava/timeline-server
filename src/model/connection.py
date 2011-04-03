import psycopg2
import psycopg2.extras

import settings

class Connection(object):
    
    def __init__(self):
        self.__connection = None
    
    def __enter__(self):
        self.__connection = psycopg2.connect(
            database=settings.config['mainDb.name'],
            user=settings.config['mainDb.user'])
        return self
    
    def __exit__(self, type, value, traceback):
        if not self.__connection is None:
            self.__connection.commit()
            self.__connection.close()
            self.__connection = None
        
    def fetchall(self, stmt, vars=None):
        cur = self.__connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        
        if vars is None:
            cur.execute(stmt)
        else:
            cur.execute(stmt, vars)
        
        return cur.fetchall()