from django.conf.urls import url
from . import views
from  django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login,name='login'),
    url(r'^logout/$', logout,name='logout'),
    url(r'^(?P<categorie>[\w|\W]+)/(?P<article_name>[\w|\W]+)',views.article,name='article')

]