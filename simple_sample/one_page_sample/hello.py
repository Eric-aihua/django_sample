# encoding: utf-8
import os
import sys

'''最简单的django 工程: 
运行方式
python hello.py runserver
'''

from django.conf import settings
DEBUG=os.environ.get('DEBUG','on')=='on'
SECRET_KEY = os.environ.get('SECRET_KEY','{{secrety_key}}')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','localhost').split(',')

settings.configure(DEBUG=DEBUG,
                   SECRET_KEY=SECRET_KEY,
				   ALLOWED_HOSTS=ALLOWED_HOSTS,
				   ROOT_URLCONF=__name__,
				   MIDDLEWARE_CLASSES=('django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',))
	

from django.conf.urls import url,include
from django.contrib import admin
from django.shortcuts import render
from django.utils.translation import ugettext
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

def index(request):
	return HttpResponse('hello word')

urlpatterns = [
    url(r'^$', index),
]
application = get_wsgi_application()

if __name__=='__main__':
    execute_from_command_line(sys.argv)
	