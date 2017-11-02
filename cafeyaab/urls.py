from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BaseView, name='base'),
    url(r'^home', views.HomeView, name='home'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^account_activation_sent$', views.account_activation_sent, name='account_activation_sent'),
]
