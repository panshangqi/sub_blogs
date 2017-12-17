# -×- coding=utf-8 -*-
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from tornado.web import RequestHandler
from jinja2 import Environment, FileSystemLoader, TemplateNotFound,ChoiceLoader
import MySQLdb
import time

from apps.essay import *
from apps.home import *
from apps.user import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

settings = {
            'debug':True,
            "cookie_secret": "bZJc2sWbQLKos6GkHnxVB9oXwQt8S0R0kRvJ5J89E=",
            "xsrf_cookies": True,
            "login_url": "/login"
        }
define('debug',default=True,help="Debug Mode",type=bool)
define("port", default=8899, help="run on the given port", type=int)

if __name__ == '__main__':
    self_dir = os.path.dirname(os.path.abspath(__file__))

    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/",HomeHandler),
            (r"/login", LoginHandler),
            (r"/logout",LogoutHandler),
            (r"/register",RegisterPageHandler),
            (r"/essay",EssayEditHandler),
            (r"/essay_upload", EssayUploadHandler),
            (r"/essay_upload_status", EssayUploadStatusHandler),
            (r"/essay_preview", EssayPreviewHandler),
            ],
        template_path = os.path.join(os.path.dirname(__file__),"templates"),
        static_path = os.path.join(os.path.dirname(__file__),"static"),
        **settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()