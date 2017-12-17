from mysql import getDBcon
from jinjaloader import *
import time

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.redirect("/")

class LoginHandler(BaseHandler):
    def get(self):
        self.render_html('login.html',message='',username='')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        db = getDBcon()
        cursor = db.cursor()
        db.set_character_set('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute("select * from users_info where username=%s and password=%s", (username, password))
        results = cursor.fetchall()
        cursor.close()
        db.close()
        if not results:
            self.render_html('login.html', message='Bad username or password', username=username)
        else:
            self.set_secure_cookie("username", self.get_argument("username"), expires_days=None, expires=time.time() + 500)
            self.redirect("/")

class RegisterPageHandler(BaseHandler):
    def get(self):
        self.render_html("register.html", username='', password='')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        repasswd = self.get_argument('repasswd')
        if username == '' or password == '' or password != repasswd:
            self.render("register.html", username=username, password=password, repasswd=repasswd)
        else:
            db = getDBcon()
            cursor = db.cursor()
            db.set_character_set('utf8')
            cursor.execute('SET NAMES utf8;')
            cursor.execute('SET CHARACTER SET utf8;')
            cursor.execute('SET character_set_connection=utf8;')
            cursor.execute("insert into users_info(username,password) values('%s','%s')" % (username, password))
            cursor.close()
            db.commit()
            db.close()
            self.render_html("login.html", message='')