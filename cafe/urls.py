from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_cafes', views.get_cafes, name='get_cafes'),
    url(r'^(?P<pk>[0-9]+)$', views.cafe, name='cafe'),
    url(r'^(?P<cafe_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/hide$', views.hide_comment, name='hide_comment'),
    url(r'^(?P<cafe_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/show', views.show_comment, name='show_comment'),
    url(r'^(?P<pk>[0-9]+)/comment$', views.comment, name='get_cafes'),
    url(r'^', views.cafes, name='cafes'),
]
