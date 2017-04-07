import json

from django.http import Http404
from django.shortcuts import render
from django.template import Context
from django.template import Template
from django.template.loader_tags import BlockNode
from django.utils._os import safe_join

__author__ = 'eric.sun'

from settings import *


def get_page_or_404(name):
    try:
        file_path = safe_join(SITE_PAGES_DIRECTORY, name)
    except BaseException, e:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')
    with open(file_path, 'r') as f:
        page = Template(f.read())

    meta = None
    for i, node in enumerate(list(page.nodelist)):
        if isinstance(node, BlockNode) and node.name == 'context':
            meta = page.nodelist.pop(i)
            break
    # print meta
    page._meta = meta
    # print dir(page)
    return page


def page(requests, slug='index'):
    # print 'slug:', slug
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {'slug': slug, 'page': page}
    if page._meta:
        meta = page._meta.render(Context())
        # print meta
        extra_context = json.loads(meta)
        context.update(extra_context)
    return render(requests, 'page.html', context)
