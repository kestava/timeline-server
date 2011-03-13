..
    Hierarchy of section markers:
    
    = with overline, for title
    =, for sections
    ^, for subsections
    -, for subsubsections

============
Installation
============

Python Virtual Environment
==========================

Create the virtual environment::

    cd /usr/local/pythonenv
    sudo virtualenv --no-site-packages KESTAVA-TIMELINE

Install gevent::

    sudo KESTAVA-TIMELINE/bin/pip install gevent
    
Install gunicorn::

    sudo KESTAVA-TIMELINE/bin/pip install gunicorn
    
.. note:: gunicorn stands for "Green Unicorn"
    
Install setproctitle::

    sudo KESTAVA-TIMELINE/bin/pip install setproctitle
    
.. note::

    gunicorn uses setproctitle to set process titles to something more
    meaningful.  Helpful when using tools like ps and top.

Install CherryPy::

    sudo KESTAVA-TIMELINE/bin/pip install cherrypy
    
Install psycopg2::

    sudo KESTAVA-TIMELINE/bin/pip install psycopg2==2.4
    
Install Upstart Script
======================

The timeline-server project includes a file called timeline-server.conf, which
is a sample Upstart script.  Copy this file to /etc/init and modify it to suit
the server (e.g. the correct path to timeline-server/src).


