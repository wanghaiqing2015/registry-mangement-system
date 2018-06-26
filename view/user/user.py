# coding: utf-8
from __future__ import unicode_literals
from import_file import *
 
from view.base.base import BaseHandler
from util.common import *
from util.function import login_required

logger = logging.getLogger(__name__)
 
class LoginHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render('login.html')
 
    @tornado.gen.coroutine
    def post(self):
        self.username = self.get_argument('username').strip()
        self.password = self.get_argument('password') 
 
        try:
            r = requests.get(self.url+'/v2/', auth=(self.username, self.password), timeout=3)
            if r.status_code==200:
                if self.username:
                    self.session["registry_username"] = self.username
                    self.session["registry_password"] = self.password
                    self.session["user"] = self.username
                else:
                    self.session["registry_username"] = "anonymous"
                    self.session["registry_password"] = "anonymous"
                    self.session["user"] = "anonymous"
                    
                self.session["registry_url"] = self.url
                self.redirect(self.reverse_url('main-images'))
            else:
                self.render("login.html", message="无法连接到镜像仓库！")
        except Exception as e:
            print(e)
            self.render("login.html", message="无法连接到镜像仓库！")
            
class LogoutHandler(BaseHandler):
    @tornado.gen.coroutine
    @login_required
    def get(self):
        self.session["user"] = None
        self.redirect('/')
 