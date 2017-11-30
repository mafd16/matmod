from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uppgift1/', views.uppgift1, name='uppgift1'),
]
