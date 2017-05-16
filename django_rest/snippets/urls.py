## -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

__author__ = 'eric.sun'

from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
schema_view = get_schema_view(title='Pastebin API')

get_test=views.SnippetViewSet.as_view({
    'get':'get_test'
})


urlpatterns = [
    # 使用API_VIEW Function定义
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    #使用APIVIEW Class 定义
    # url(r'^$', views.api_root),
    # url(r'^snippets/$', views.SnippetList.as_view(),name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view(),name='snippet-detail'),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',views.SnippetHighlight.as_view(), name='snippet-highlight'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    #
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    #############################################使用Model class
    url(r'^', include(router.urls)),
    url(r'^snippets/get_test', get_test),
    url(r'^schema/$', schema_view),
]

# urlpatterns = format_suffix_patterns(urlpatterns)