"""
WSGI config for naulo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys, site

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
WORK_DIRECTORY = os.path.join(CURRENT_DIRECTORY, '..')

#Add the site-packages
site.addsitedir('/home/techkunja/www/envs/naulo_env/lib/python3.5/site-packages')

#adding the project to the python path
sys.path.append(WORK_DIRECTORY)
#adding the parent directory to the python path
sys.path.append(os.path.join(WORK_DIRECTORY, '..'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "naulo.settings")

application = get_wsgi_application()
