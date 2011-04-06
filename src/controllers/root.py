import json
from pprint import pprint

import cherrypy

from model.database import Database

class Root(object):
    
    @cherrypy.expose
    def public(self, **kwargs):

        self.__assert_argument('callback', kwargs)
        self.__assert_argument('maxCount', kwargs)
        
        entries = Database.get_messages(kwargs['maxCount'])
        return self.__get_jsonp_response(kwargs['callback'], entries)
        
    def __get_jsonp_response(self, callback, data):
        return '{0}({1})'.format(callback, json.dumps(data))
        
    def __assert_argument(self, name, testArgs):
        if not name in testArgs:
            raise cherrypy.HTTPError(
                400,
                message='The web service requires a "{0}" argument'.format(name))