# coding: utf-8
from __future__ import unicode_literals
from import_file import *

from view.user.user import *
 
user_urls=[
        url(r"/login/", LoginHandler, name="login"),
        url(r"/logout/", LogoutHandler, name="logout"),
    ]