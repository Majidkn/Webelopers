from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView, name='base'),
    url(r'^profiles/(?P<pk>[\w-]+)', views.profiles, name='profiles'),
    url(r'^profile/add_cafe', views.add_cafe, name='add_cafe'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^account_activation_sent$', views.account_activation_sent, name='account_activation_sent'),
]
