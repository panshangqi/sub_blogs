from mysql import getDBcon
from jinjaloader import *
import time

class HomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        page_id = self.get_argument('page_id', 1)
        page_rows = self.get_argument('page_rows', 10)
        min_id = (page_id - 1) * 10 + 1
        max_id = min_id + page_rows - 1
        db = getDBcon()
        cursor = db.cursor()
        db.set_character_set('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')

        cursor.execute("select user_id from users_info where username='%s'" % (username))
        first = cursor.fetchone()
        user_id = first[0]

        cursor.execute("select blog_uuid,blog_title,blog_summary,blog_time from about_blog where blog_user_id='%d' order by blog_time desc" % (user_id))
        results = cursor.fetchall()
        article_lists = []
        count = 0
        for row in results:
            count = count + 1
            if count >= min_id and count <= max_id:
                dict = {}
                dict['blog_uuid'] = row[0]
                dict['blog_title'] = row[1]
                dict['blog_summary'] = row[2]
                timeStamp = row[3]
                timeArray = time.localtime(timeStamp)
                formatTime = time.strftime("%Y-%m-%d:%H:%M:%S",timeArray)
                dict['blog_time'] = formatTime
                article_lists.append(dict)
        article_lists.sort(key=lambda obj:obj.get('blog_time'), reverse=True)
        self.render_html("home.html", username=username, page_id=page_id, article_lists=article_lists)


