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
        
        entries = Database.get_last_n_messages(kwargs['maxEntries'])
        return '{0}({1})'.format(kwargs['callback'], entries)