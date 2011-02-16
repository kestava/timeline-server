"""
Timeline server

Serves near real-time timeline data to web clients who connect using Comet
"long polling" methods
"""

from pprint import pprint
import json

import cherrypy
import psycopg2

class Server(object):
    
    @cherrypy.expose
    def public(self, **kwargs):
        pprint(kwargs)
        
        if 'maxEntries' in kwargs:
            entries = self.get_n_entries(kwargs['maxEntries'])
        else:
            entries = self.get_all_entries()
        
        pprint(entries)
        
        return '{0}({1})'.format(kwargs['callback'], entries)
    
    def get_n_entries(self, n):
        """
        Read that last n entries from the database.
        """
        data = 'blah'

        
        return json.dumps(data)
        
    def get_all_entries(self):
        raise Exception('blah')
        
app = cherrypy.tree.mount(Server())
