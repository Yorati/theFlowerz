from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flowers/$', views.FlowerListView.as_view(), name='flowers'),
    url(r'^flower/(?P<pk>\d+)$', views.FlowerDetailView.as_view(), name='flower-detail'),
]
urlpatterns += [
    url(r'^myflowers/$', views.LoanedFlowersByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [
    url(r'^signup/$', views.signup, name='signup'),
]
