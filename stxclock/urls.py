from django.conf.urls import url, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from stxclock.views import ExchangeViewSet, UserViewSet, api_root


exchange_list = ExchangeViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })
exchange_detail = ExchangeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    })
user_list = UserViewSet.as_view({
    'get': 'list'
    })
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
    })


# app_name = 'stxclock'
urlpatterns = format_suffix_patterns([
        url(r'^$', api_root),
        url(r'^exchanges/$', exchange_list, name='exchange-list'),
        url(r'^exchanges/(?P<pk>[0-9]+)/$', exchange_detail, name='exchange-detail'),
        url(r'^users/$', user_list, name='user-list'),
        url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
        ])

# Login and logout views for the browsable API
urlpatterns += [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        ]
