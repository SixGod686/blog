from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^new/$',views.new,name='new'),
    url(r'^newlist/$',views.newlist,name='newlist'),
    url(r'^share/$',views.share,name='share'),
    url(r'^login/$',views.login,name='login'),
]