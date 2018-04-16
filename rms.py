# coding: utf-8
from __future__ import unicode_literals
from import_file import *

# for pyinstaller 
if hasattr(sys, "_MEIPASS"):
    os.chdir(sys._MEIPASS)
else:
    os.chdir( os.path.dirname( os.path.abspath(__file__)) )
 
logger = logging.getLogger(__name__)
from util import log_config
log_config.init( )  # 必须放在app初始化的前面， 否则别的模块识别不到
 
from application import Application
 
define("port", default=50000, help="run on the given port", type=int)
 
if __name__=='__main__':  
    tornado.options.parse_command_line()
   
    tornado_app = Application()     
    http_server = tornado.httpserver.HTTPServer(
        request_callback=tornado_app,
    )
 
    http_server.bind(
        port=options.port, 
        address="0.0.0.0",
    )    
    http_server.start(num_processes=1) 
 
    server = tornado.ioloop.IOLoop.instance()
    print('service start running on 0.0.0.0:{0}'.format(options.port))
    
    try:
        url = "http://127.0.0.1:50000/"
        server.add_callback(webbrowser.open, url)
    except:
        pass
    server.start()
 

 
 