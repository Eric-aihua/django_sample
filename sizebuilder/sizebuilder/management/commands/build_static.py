import os
import shutil

from django.core.management import BaseCommand, call_command
from django.test import Client
from django.urls import reverse

from sizebuilder import settings

__author__ = 'eric.sun'


def get_pages():
    for name in os.listdir(settings.SITE_PAGES_DIRECTORY):
        if name.endswith('.html'):
            yield name[:-5]


class Command(BaseCommand):
    help = 'Build static site output'
    leave_locale_alone = True

    def handle(self, *args, **options):
        settings.DEBUG=False
        if os.path.exists(settings.SITE_OUTPUT_DIRECTORY):
            shutil.rmtree(settings.SITE_OUTPUT_DIRECTORY)
        os.mkdir(settings.SITE_OUTPUT_DIRECTORY)
        os.makedirs(settings.STATIC_ROOT)
        call_command('collectstatic',interactive=False,clear=True,verbosity=0)
        client=Client()
        for page in get_pages():
            url=reverse('page',kwargs={'slug':page})
            response=client.get(url)
            if page=='index':
                output_dir=settings.SITE_OUTPUT_DIRECTORY
            else:
                output_dir=os.path.join(settings.SITE_OUTPUT_DIRECTORY,page)
                os.makedirs(output_dir)
            with open(os.path.join(output_dir,'index.html'),'wb') as f:
                f.write(response.content)
