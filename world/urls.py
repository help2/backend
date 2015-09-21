from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^places/$', views.places, name='index'),
]

admin.site.site_header = 'helphelp2'
admin.site.index_title = ' '
