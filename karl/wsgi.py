import os
import sys
import django

# Add the parent directory to Python's module search path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Force ALLOWED_HOSTS via environment variable
os.environ['DJANGO_ALLOWED_HOSTS'] = 'swiftdocx.co.ke,www.swiftdocx.co.ke,.vercel.app'

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karl.settings')

# --- DEBUGGING SECTION ---
# This will print directly to the Vercel runtime logs
print(f"*** LOADED WSGI FROM: {__file__} ***", file=sys.stderr)

django.setup()
from django.conf import settings
print(f"*** DJANGO SETTINGS FILE IN USE: {settings.SETTINGS_MODULE} from {settings.__file__} ***", file=sys.stderr)
print(f"*** FINAL ALLOWED_HOSTS VALUE: {settings.ALLOWED_HOSTS} ***", file=sys.stderr)
# --- END DEBUGGING SECTION ---

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()