# coding: utf8
from import_file import *
 
logger = logging.getLogger(__name__)

def get_images_list(self):
    r = requests.get(self.url+'/v2/_catalog', auth=(self.username, self.password))
    return r.json()['repositories']
    
def get_labels_list(self, image):
    r = requests.get(self.url+'/v2/%s/tags/list'%image, auth=(self.username, self.password))
    tags = r.json()['tags']
    return tags if tags else []
    
def get_label(self, image, tag):
    r = requests.get(self.url+'/v2/%s/manifests/%s'%(image, tag), auth=(self.username, self.password) )
 
    name = r.json()['name']
    v1Compatibility = r.json()['history'][0]['v1Compatibility']
    return name, v1Compatibility
    
def get_digest(self, image, tag):
    headers = { "Accept": "application/vnd.docker.distribution.manifest.v2+json"}
    r = requests.get(self.url+'/v2/%s/manifests/%s'%(image, tag), auth=(self.username, self.password), headers=headers)
    
    Digest = r.headers['Docker-Content-Digest'].strip()
    return Digest 
    
def delete_label(self, image, tag):
    digest = get_digest(self, image, tag)
 
    r = requests.delete(self.url+'/v2/%s/manifests/%s'%(image, digest), auth=(self.username, self.password))
 
    if r.status_code == 202:
        return True
    else:
        return False
    
'''
{'architecture': 'amd64',
 'author': 'whq <krman@163.com>',
 'config': {'ArgsEscaped': True,
            'AttachStderr': False,
            'AttachStdin': False,
            'AttachStdout': False,
            'Cmd': ['/bin/sh', '-c', 'python3 aim.py'],
            'Domainname': '',
            'Entrypoint': None,
            'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
            'ExposedPorts': {'12133/tcp': {}},
            'Hostname': '68ad5a47a9a7',
            'Image': 'sha256:149efeb51c40f7d52dc94af35fda24e3e44b789a88c4d9da3a61d2f7e13133cd',
            'Labels': {},
            'OnBuild': [],
            'OpenStdin': False,
            'StdinOnce': False,
            'Tty': False,
            'User': '',
            'Volumes': None,
            'WorkingDir': '/aim'},
 'container': 'f8ab1bb5d3f5332ff21ab51827528c60c4e19bf816879a0e641f12f7140524a6',
 'container_config': {'ArgsEscaped': True,
                      'AttachStderr': False,
                      'AttachStdin': False,
                      'AttachStdout': False,
                      'Cmd': ['/bin/sh',
                              '-c',
                              '#(nop) ',
                              'CMD ["/bin/sh" "-c" "python3 aim.py"]'],
                      'Domainname': '',
                      'Entrypoint': None,
                      'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
                      'ExposedPorts': {'12133/tcp': {}},
                      'Hostname': '68ad5a47a9a7',
                      'Image': 'sha256:149efeb51c40f7d52dc94af35fda24e3e44b789a88c4d9da3a61d2f7e13133cd',
                      'Labels': {},
                      'OnBuild': [],
                      'OpenStdin': False,
                      'StdinOnce': False,
                      'Tty': False,
                      'User': '',
                      'Volumes': None,
                      'WorkingDir': '/aim'},
 'created': '2018-04-08T06:57:51.1638031Z',
 'docker_version': '1.13.1',
 'id': '8bc68c7e08adb53642096c5bc6c748b11184670613ee0fdc10571a461ca6defe',
 'os': 'linux',
 'parent': 'db70a3ffbe7ae17df0386fe95ce51fdd74cd81785bd883caddc56db5425fb3bc',
 'throwaway': True}
'''