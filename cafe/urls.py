from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_cafes', views.get_cafes, name='get_cafes'),
    url(r'^(?P<pk>[0-9]+)$', views.cafe, name='cafe'),
    url(r'^(?P<cafeId>[0-9]+)/comments/(?P<commentId>[0-9]+)/hide$', views.hideComment, name='hide_comment'),
    url(r'^(?P<cafeId>[0-9]+)/comments/(?P<commentId>[0-9]+)/show', views.showComment, name='show_comment'),
    url(r'^(?P<pk>[0-9]+)/comment$', views.comment, name='get_cafes'),
    url(r'^(?P<cafeid>[0-9]+)/favit$', views.favit, name='favit'),
    url(r'^', views.cafes, name='cafes'),
]
