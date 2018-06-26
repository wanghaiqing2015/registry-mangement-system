# coding: utf-8
from __future__ import unicode_literals
from import_file import *
 
from view.base.base import BaseHandler
from util.common import *
from util.function import login_required

logger = logging.getLogger(__name__)
 
class LabelHandler(BaseHandler):
    @tornado.gen.coroutine
    @login_required
    def get(self, image):
        self.image = image
        
        data = yield self.async_do(self.asynchronous) 
        self.render('label.html', **data)
 
    def asynchronous(self):
        labels = get_labels_list(self, self.image)
        labels = [{'name':i} for i in labels]
        
        for i in labels:
            image, label = get_label(self, self.image, i['name'])
            
            label = json.loads(label)
 
            i['architecture'] = label['architecture']
            i['author'] = label['auther'] if 'auther' in label else ''
            i['docker_version'] = label['docker_version']
            i['Cmd'] = label['config']['Cmd'] if 'Cmd' in label['config'] else ''
            i['ExposedPorts'] = label['config']['ExposedPorts'] if 'ExposedPorts' in label['config'] else ''
            i['created'] = label['created']
            i['id'] = label['id'][0:12]
            i['Volumes'] = label['config']['Volumes'] if 'Volumes' in label['config'] else ''
            i['WorkingDir'] = label['config']['WorkingDir'] if 'WorkingDir' in label['config'] else ''
            i['image'] =  image
            
        data = {
            'labels': labels,
            'num_labels': len(labels),
        }
 
        return data
        
class DeleteLabelHandler(BaseHandler):
    @tornado.gen.coroutine
    @login_required
    def delete(self):
        image = self.get_argument('image')
        tag = self.get_argument('tag')
        data = delete_label(self, image, tag)
 
        if data:
            self.write_success()
        else:
            self.write_fail()
 
    