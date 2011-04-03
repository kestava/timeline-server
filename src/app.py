"""
Timeline server

Serves near real-time timeline data to web clients who connect using Comet
"long polling" methods
"""

import cherrypy

from controllers.root import Root
from lib.applogging import setup_logging

#cherrypy.config.update({'environment': 'embedded'})

def get_configuration():
    serverConfig = {
        '/': {}
    }
    
    return serverConfig

setup_logging()
    
app = cherrypy.tree.mount(root=Root(), config=get_configuration())
