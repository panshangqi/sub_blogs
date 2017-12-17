# -×- coding=utf-8 -*-

import time
from jinjaloader import *
from mysql import getDBcon
from article_edit import SummaryHTMLParser
import uuid
class EssayEditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render_html("essay.html")

class EssayDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        p=0

class EssayUploadStatusHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        status = self.get_argument('status')
        blog_uuid = self.get_argument('blog_uuid')
        self.render_html('essay_upload_status.html',status=status, blog_uuid=blog_uuid)

class EssayPreviewHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        blog_uuid = self.get_argument('blog_uuid')
        db = getDBcon()
        cursor = db.cursor()
        db.set_character_set('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute("select blog_title,blog_article,blog_time from about_blog where blog_uuid='%s'" % (blog_uuid))
        first = cursor.fetchone()
        blog_title = first[0]
        blog_article = first[1]
        blog_time = first[2]
        self.render_html('essay_preview.html',blog_title=blog_title,blog_article=blog_article,blog_time=blog_time)

class EssayUploadHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        username = self.get_secure_cookie("username")
        db = getDBcon()
        cursor = db.cursor()
        db.set_character_set('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute("select user_id from users_info where username='%s'" % (username))
        first = cursor.fetchone()
        blog_user_id = first[0]
        print blog_user_id
        blog_uuid = str(uuid.uuid1())
        blog_time = time.time()
        blog_title = self.get_argument("blog_title")
        blog_article = self.get_argument("blog_article")
        parser = SummaryHTMLParser(150)
        parser.feed(blog_article)
        blog_summary = parser.get_summary(u'...' ,u'')
        try:
            cursor.execute \
            ("insert into about_blog(blog_user_id,blog_time,blog_uuid,blog_title,blog_summary,blog_article) "
             "values('%d','%d','%s','%s','%s','%s')" %
            (blog_user_id, blog_time, blog_uuid, blog_title, blog_summary, blog_article))
            db.commit()
            print '1'
            dict = {}
            dict['status'] = 'true'
            dict['blog_uuid'] = blog_uuid
            print '2'
            print dict
            self.write(dict)
        except:
            dict = {}
            dict['status'] = 'false'
            dict['blog_uuid'] = ''
            self.write(dict)




