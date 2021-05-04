"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application, WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

application: WSGIHandler = get_wsgi_application()
