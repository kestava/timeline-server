"""
This is the database module.
"""
from pprint import pprint
import logging
import json

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
            return cnx.fetch_all("""
                select
                    m.message_id,
                    m.message_text,
                    kestava.to_iso_8601_string(m.created_when) as created_when_formatted,
                    m.ref_account_id,
                    a.email
                from kestava.messages as m
                    left join kestava.accounts as a on m.ref_account_id = a.account_id
                order by
                    m.created_when desc,
                    m.message_id desc
                limit %s;""",
                (max,))
                
                