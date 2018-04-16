# coding: utf-8
from __future__ import unicode_literals
from import_file import *
 
logger = logging.getLogger(__name__)
 
class BaseHandler(SessionBaseHandler):
    def access_control_allow(self): # 允许 JS 跨域调用
        self.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Depth, User-Agent, X-File-Size, "
                                                        "X-Requested-With, X-Requested-By, If-Modified-Since, "
                                                        "X-File-Name, Cache-Control, Token")
        self.set_header('Access-Control-Allow-Origin', '*')
        
    def get_current_user(self):
        current_user = self.session.get('user',None) # 必须开启 xsrf_cookies
        return current_user
 
    def initialize(self):
        self.request.headers['X-Xsrftoken'] = tornado.escape.to_unicode(self.xsrf_token)
 
        self.thread_executor = ThreadPoolExecutor(300)
        self.async_do = self.thread_executor.submit
 
    @tornado.gen.coroutine
    def prepare(self):
        logger.info("请求:")
        logger.info("   remote_ip   : " + self.request.remote_ip)
        logger.info("   method      : " + self.request.method)
        logger.info("   uri         : " + self.request.uri)
        logger.info("   time        : " + time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime(time.time())))
        
        if self.get_current_user():
            self.username = self.session["registry_username"]
            self.password = self.session["registry_password"]
            self.url = self.session["registry_url"]
        if 'registry_url' in self.session:
            self.registry_url = self.session["registry_url"]
            if 'http' in self.registry_url:
                self.registry_url = self.session["registry_url"].split('://')[1]
        else:
            self.registry_url = self.request.headers['Host']
 
    @tornado.gen.coroutine
    def on_finish(self):
        pass
 
    def write_error(self, status_code, **kwargs):
        if status_code == 403:
            self.render("403.html")
        elif status_code == 404 or 405:
            self.render("404.html")
        elif status_code == 500:
            self.render("500.html")
 
    def write_success(self, data={}, message=''):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write({"status": True, "data": data, "message": message})
        raise Finish  # 确保后面的代码不会执行

    def write_fail(self, data={}, message=''):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write({"status": False, "data": data, "message": message})
        raise Finish  # 确保后面的代码不会执行
 