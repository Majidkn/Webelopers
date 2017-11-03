from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView, name='base'),
    url(r'^home', views.HomeView, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<userId>[0-9]+)/delete_image$', views.delete_image, name='account_delete_image'),
    url(r'^profile/add_cafe$', views.add_cafe, name='add_cafe'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^profiles/(?P<pk>[\w-]+)', views.profiles, name='profiles'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^account_activation_sent$', views.account_activation_sent, name='account_activation_sent'),
]
