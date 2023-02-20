# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/z/zakhar9k/zakhar9k.beget.tech/blagodarenie')
sys.path.insert(1, '/home/z/zakhar9k/zakhar9k.beget.tech/blagoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'blagodarenie.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()