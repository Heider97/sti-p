#!/usr/bin/python
import sys
sys.path.insert(0, 'var/www/html/sti-p')
from flaskapp import app as application
application.secret_key = 'stip'