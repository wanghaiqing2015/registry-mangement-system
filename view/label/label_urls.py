# coding: utf-8
from __future__ import unicode_literals
from import_file import *

from view.label.label import *
 
label_urls=[
        url(r"/labels/(?P<image>.+)/", LabelHandler, name="labels"),
        url(r"/delete_label/", DeleteLabelHandler, name="delete_label"),
    ]