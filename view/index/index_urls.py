# coding: utf-8
from __future__ import unicode_literals
from import_file import *

from view.index.index import *
 
index_urls=[
        url(r"/", IndexHandler, name="main-images"),
        url(r"/images/(?P<sort>.+)/(?P<order>.+)/", IndexHandler, name="images"),
    ]