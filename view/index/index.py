# coding: utf-8
from __future__ import unicode_literals
from import_file import *
 
from view.base.base import BaseHandler
from util.common import *
from util.function import login_required

logger = logging.getLogger(__name__)
 
class IndexHandler(BaseHandler):
    @tornado.gen.coroutine
    @login_required
    def get(self, sort='name', order='desc'):
        self.sort = sort
        self.order = order
        
        data = yield self.async_do(self.asynchronous) 
        self.render('index.html', **data)
 
    def asynchronous(self):
        images = get_images_list(self)
        images = [{'name':i} for i in images]
    
        images.sort(
            key=lambda x: x.get(self.sort),
            reverse=True if self.order != 'asc' else False
        )
 
        data = {
            'images': images,
            'num_images': len(images),
            'sort': self.sort,
            'order': self.order,
        }
 
        return data
      