import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

# Get the WSGI application
app = get_wsgi_application()

def handler(event, context):
    """
    Vercel serverless handler for Django application
    """
    # This is a basic handler - for full Django support on Vercel,
    # consider using a framework like Vercel Django or serverless functions
    return {
        'statusCode': 200,
        'body': 'Hello from Django on Vercel!'
    }
