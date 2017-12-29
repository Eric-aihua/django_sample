# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from django.test import Client
from django.test import TestCase

# Create your tests here.
#from rest_framework import settings
import os
import sys
sys.path.append('F:\\Sourcecode\\github\\django_sample\\django_rest')
print sys.path
import django_rest.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_rest.settings")
from rest_framework.test import APIRequestFactory, RequestsClient

class Test(TestCase):

    def test_get(self):
        client=Client()
        response=client.get('http://127.0.0.1:8000/snippets/')
        print response.response_code()

if __name__ == '__main__':
    unittest.main()