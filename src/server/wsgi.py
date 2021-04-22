import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.append('/home/ubuntu/bms/src')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()
