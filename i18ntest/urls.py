from django.conf.urls import url

from . import views
# set url namespace
app_name = 'i18ntest'

# ===============================view method=====================================
urlpatterns = [
     url(r'^$', views.index, name='index'),
	 url(r'^reset$', views.reset, name='reset'),
     # ex: /polls/
	 ]


