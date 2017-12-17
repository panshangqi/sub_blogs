
import MySQLdb
def getDBcon():
    return MySQLdb.connect('www.pansq.xyz',"root","pansq123456","blogs")
