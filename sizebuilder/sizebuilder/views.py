from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join

__author__ = 'eric.sun'

from settings import *

def get_page_or_404(name):
    try:
        file_path=safe_join(SITE_PAGES_DIRECTORY,name)
    except BaseException,e:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')
    with open(file_path,'r') as f:
        page=Template(f.read())
    return page

def page(requests,slug='index'):
    print 'slug:',slug
    file_name='{}.html'.format(slug)
    page=get_page_or_404(file_name)
    context={'slug':slug,'page':page}
    return render(requests,'page.html',context)
