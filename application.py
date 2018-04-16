# coding: utf-8
from __future__ import unicode_literals
from import_file import *

import util.uimethods
from url_mapping import handlers
 
# 继承tornado.web.Application类，可以在构造函数里做站点初始化（初始数据库连接池，初始站点配置，初始异步线程池，加载站点缓存等）
class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            handlers=handlers,
            debug=False,
            autoreload=True if system()=="Windows" else False ,  # 应用程序将会观察它的源文件是否改变，并且当任何文件改变的时候便重载它自己。 
            compiled_template_cache=False,  # False html修改， 立即生效
            static_hash_cache=True, # False 静态文件哈希 (被 static_url 函数使用) 将不会被缓存。 True  不会每次都下载静态文件
            template_path="templates",
            static_path="static",
            cookie_secret=os.urandom(64),# 注释掉后， get_secure_cookie 不能用了
            xsrf_cookies=True, # 目前开启后， python3 会报错，2不会。api POST 调用失败，报错：'_xsrf' argument missing from POST. 已经解决了， tornado.escape.to_unicode(self.xsrf_token)
            ui_methods=util.uimethods,
            session = {# torndsession->memory
                'driver':'memory',
                'driver_settings':{'host': self},
                'force_persistence':True,
                'sid_name':'torndsessionID',
                'session_lifetime':60*60*24*7,
                'cookie_config': {
                    'expires_days': 7,  # 优先级其次
                },
            },
        )
        tornado.web.Application.__init__(self, **settings)
 

