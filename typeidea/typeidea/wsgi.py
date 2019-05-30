"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.envsiron.get('TYPEIDEA_PROFILE', 'develop')
os.envviron.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.setting.%s" % profile)

application = get_wsgi_application()