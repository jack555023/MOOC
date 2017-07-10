# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import password_change_done
from .views import *


urlpatterns = [
    url(r'^$', home, name='home', ),
    url(r'^addcourses/$', addcourses, name='addcourses', ),
    url(r'^deleteCourses/(?P<pk>\d+)/$', deleteCourses, name='deleteCourses', ),
    url(r'^keywords/(?P<pk>\d+)/$',keywords, name='keywords',),
    url(r'^deletekeywords/(?P<pk>\d+)/$',deletekeywords, name='deletekeywords', ),
    url(r'^addkeywords/(?P<pk>\d+)$',addkeywords, name='addkeywords', )
]
