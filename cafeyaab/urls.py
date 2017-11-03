from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BaseView, name='base'),
    url(r'^home', views.HomeView, name='home'),
    url(r'^profile/(?P<userId>[0-9]+)/delete_image$', views.delete_image, name='account_delete_image'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^editprofile', views.editprofile, name='editprofile'),
    url(r'^account_activation_sent$', views.account_activation_sent, name='account_activation_sent'),
]
