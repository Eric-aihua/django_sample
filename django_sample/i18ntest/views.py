from django.shortcuts import render
from django.utils.translation import ugettext
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)
def index(request):
	return render(request, 'i18ntest/index.html')

def reset(request):
	logger.info('debug info')
	return render(request, 'i18ntest/i18nreset.html')

