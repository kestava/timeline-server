import json
from pprint import pprint

import cherrypy

from model.database import Database

class Root(object):
    
    @cherrypy.expose
    def public(self, **kwargs):
    
        if not 'callback' in kwargs:
            raise cherrypy.HTTPError(
                400,
                message='The web service requires a "callback" argument')
        
        if not 'maxEntries' in kwargs:
            raise cherrypy.HTTPError(
                400,
                message='The web service requires a "maxEntries" argument')
            
        if 'since' in kwargs:
            # extract the date
            pass
        
        entries = Database.get_messages(kwargs['maxEntries'])
        pprint(entries)
        s = json.dumps(entries)
        print(s)
        return '{0}({1})'.format(kwargs['callback'], s)