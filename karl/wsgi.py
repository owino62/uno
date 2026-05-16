import os
import sys

# Add parent directory to path so Python finds the 'karl' module
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Force ALLOWED_HOSTS via environment variable
os.environ['DJANGO_ALLOWED_HOSTS'] = 'swiftdocx.co.ke,www.swiftdocx.co.ke,.vercel.app'

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'karl.settings')

# Optional: simple debug to confirm (no .__file__)
print(f"*** WSGI loaded, DJANGO_ALLOWED_HOSTS = {os.environ.get('DJANGO_ALLOWED_HOSTS')} ***", file=sys.stderr)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()