# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import password_change_done
from .views import *


urlpatterns = [
    url(r'^signup/', signup_view, name='signup', ),
    url(r'^valid/', valid_view, name='valid', ),
    url(r'^login/', login_view, name='login', ),
    url(r'^logout/', logout_view, name='logout', ),
    # url(r'^password-change/$', password_change_view, name='password_change'),
    # url(r'^password-change/done/$',
    #     password_change_done, name='password_change_done'),
]
