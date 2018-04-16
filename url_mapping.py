# coding: utf-8
from __future__ import unicode_literals
from import_file import *

from view.index.index_urls import index_urls
from view.label.label_urls import label_urls
from view.user.user_urls import user_urls

handlers=[]
         
handlers += index_urls
handlers += label_urls
handlers += user_urls
 