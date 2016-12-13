from django.conf.urls import url
from . import views
from  django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login',UserCreationForm)
]