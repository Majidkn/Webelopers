from django.conf.urls import url

from cafeyaab.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
