from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uppgift1/', views.uppgift1, name='uppgift1'),
    url(r'^uppgift2/', views.uppgift2, name='uppgift2'),
    url(r'^uppgift3/', views.uppgift3, name='uppgift3'),
]
