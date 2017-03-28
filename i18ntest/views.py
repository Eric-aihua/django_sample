from django.shortcuts import render
from django.utils.translation import ugettext
from django.http import HttpResponse

def index(request):
	return render(request, 'i18ntest/index.html')

