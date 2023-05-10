from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^owners/$', views.OwnerListView.as_view(), name='owners'),
    re_path(r'^notowners/$', views.NotownerListView.as_view(), name='notowners'),
    re_path(r'^ads/$', views.AdsListView.as_view(), name='ads'),
    re_path(r'^indicators/$', views.IndicatorsListView.as_view(), name='indicators'),
]

#update, create, delete ads
urlpatterns += [
    re_path(r'^ads/create/$', views.AdsCreate.as_view(), name='ads_create'),
    re_path(r'^ads/(?P<pk>\d+)/update/$', views.AdsUpdate.as_view(), name='ads_update'),
    re_path(r'^ads/(?P<pk>\d+)/delete/$', views.AdsDelete.as_view(), name='ads_delete'),
]
#update, create, delete owners
urlpatterns += [
    re_path(r'^client/create/$', views.OwnerCreate.as_view(), name='owner_create'),
    re_path(r'^client/(?P<pk>\d+)/update/$', views.OwnerUpdate.as_view(), name='owner_update'),
    re_path(r'^client/(?P<pk>\d+)/delete/$', views.OwnerDelete.as_view(), name='owner_delete'),
]
#update, create, delete notowners
urlpatterns += [
    re_path(r'^fix/create/$', views.NotownerCreate.as_view(), name='notowner_create'),
    re_path(r'^fix/(?P<pk>\d+)/update/$', views.NotownerUpdate.as_view(), name='notowner_update'),
    re_path(r'^fix/(?P<pk>\d+)/delete/$', views.NotownerDelete.as_view(), name='notowner_delete'),
]

#update, create, delete indicators
urlpatterns += [
    re_path(r'^worker/create/$', views.IndicatorsCreate.as_view(), name='indicators_create'),
    re_path(r'^worker/(?P<pk>\d+)/update/$', views.IndicatorUpdate.as_view(), name='indicators_update'),
    re_path(r'^worker/(?P<pk>\d+)/delete/$', views.IndicatorsDelete.as_view(), name='indicators_delete'),
]