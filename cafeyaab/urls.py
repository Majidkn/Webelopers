from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BaseView, name='base'),
    url(r'^home', views.HomeView, name='home'),
]
