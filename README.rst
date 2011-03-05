Configuration
=============

To configure, create src/config.py by copying src/config.py.sample and modify
runtime variables:

    * bind: set to the appropriate network interface IP address and port

.. warning:: The following information about running the server from the command
   line is deprecated in favor of using a monitoring agent.  See the *Upstart*
   section below.

To run the server *in development*, from within the src directory::

    sudo -u kestava /usr/local/pythonenv/KESTAVA-TIMELINE/bin/gunicorn -c config.py app:app

The worker processes are governed by the "arbiter" process, which can be managed
by sending it signals using the *kill* command.

To restart workers::

    sudo kill -HUP <masterpid>

To terminate all processes::

    sudo kill -SIGQUIT masterpid
    
Information about running processes, including the masterpid can be obtained
with the following command::

    ps -ef | grep timeline-server
    
The masterpid can be isolated like this::

    pidof 'gunicorn: master [timeline-server]'
    
Upstart
=======

When managed by Upstart, you should prefer the initctl commands over sending
signals directly.

To restart workers::

    sudo reload timeline-server
    
To stop the arbiter process (and all workers)::

    sudo stop timeline-server
    
To start the arbiter process::

    sudo start timeline-server
    
To check the status of the arbiter process::

    sudo initctl status timeline-server
