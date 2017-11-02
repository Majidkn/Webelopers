from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_cafes', views.get_cafes, name='get_cafes'),
    url(r'^(?P<pk>[0-9]+)$', views.cafe, name='cafes'),
    url(r'^', views.cafes, name='cafes'),
]
