import sys, os
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "karrlab.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

from karrlab import monitor
monitor.start(interval = 1.0)

#from paste.exceptions.errormiddleware import ErrorMiddleware
#application = ErrorMiddleware(_application, debug=True)
