
To configure, create src/config.py by copying src/config.py.sample and modify
runtime variables:

    * bind: set to the appropriate network interface IP address and port

To run the server *in development*, from within the src directory::

    sudo -u kestava /usr/local/pythonenv/KESTAVA-TIMELINE/bin/gunicorn -c config.py server:app