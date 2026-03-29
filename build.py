#!/usr/bin/env python
"""
Build script for Vercel deployment
Generates static HTML files for the portfolio site
"""
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

# Add project to path
sys.path.insert(0, os.path.dirname(__file__))

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    # Collect static files
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])

    # You can add additional build steps here
    print("Build completed successfully!")