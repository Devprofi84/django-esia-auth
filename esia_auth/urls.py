# -*- coding: utf-8 -*-
from django.urls import path
from django.conf import settings
from django.utils.module_loading import import_string

from .views import esia_login_view, esia_oauth_link_view


login_view_path = getattr(settings, 'ESIA_LOGIN_VIEW', None)
if login_view_path:
    login_view = import_string(login_view_path)
else:
    login_view = esia_login_view


urlpatterns = [
    path(r'login/$', login_view, name='login'),
    path(r'oauth-link/$', esia_oauth_link_view, name='link'),
]
