import threading
import MySQLdb
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText
import log
import urllib

def get_conn():
    con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='logsdb',port=3306,charset='utf8')
    return con

def calculate_time():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return now

def get_data():
    sql = "select message from logs where level = 3"
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def task():
    while True:
        results = get_data()
        for id in range(len(results)):
            print results[id]
        time.sleep(1)
    
def run_monitor():
    monitor = threading.Thread(target=task)
    monitor.start()
    
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if __name__ == "__main__":
    print getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0")
