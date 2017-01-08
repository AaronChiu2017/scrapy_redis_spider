#-*-coding:utf-8-*-
import pymysql
import redis
import json
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from tornado import gen

class SQL(object):
    def __init__(self, user, passwd, host, db, charset='utf8', 
		         cursorclass=pymysql.cursors.DictCursor):
	    self.kw = {'user':user,
	               'passwd':passwd,
	               'host':host,
	               'db':db,
	               'charset':charset,
	               'cursorclass':cursorclass}
	    self.conn = self._connect()

    def _connect(self):
        return pymysql.connect(**self.kw)

    def table(self):
    	cmd = """CREATE TABLE douban 
    				(id int NOT NULL AUTO_INCREMENT,
    				movie_name varchar(255),
    				movie_type varchar(255),
    				movie_year varchar(255),
    				movie_rate varchar(255),
    				PRIMARY KEY (id)
    				);"""

    	with self.conn.cursor() as cursor:
    		cursor.execute(cmd)
    		self.conn.commit()

    def insert(self, cmd, items=()):
        with self.conn.cursor() as cursor:
        	try:
        	    cursor.execute(cmd, items)
        	    self.conn.commit()
        	except Exception as e:
        		print(e)
        		raise

    def select(self, cmd, items=()):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(cmd, items)
            except Exception as e:
                print(e)
                raise
            else:
                return cursor.fetchall()

    def close(self):
    	self.conn.close()


@gen.coroutine
def main():
    rc = redis.StrictRedis(host='localhost', password='')
    pipe = rc.pipeline()
    q = Queue()
    db = SQL('root', '', 'localhost', 'douban')
	
    #db.table()
	
    count = 50

    @gen.coroutine
    def enqueue():
        while 1:
            for x in range(count):
                pipe.rpop('myspider:items')
            items = pipe.execute()#返回的是一个列表
            #print(items)
            if any(items):
                for item in items:
                	if item:
                		item = item if isinstance(item, str) else item.decode()
                		yield q.put(item)
                	else:
                		pass
            else:
                yield q.put(1)
                break


    @gen.coroutine
    def dequeue():
        while 1:
            item = yield q.get()
            if item != 1:
                #print(item)
                #子类dict,自定义__missing__方法，用来处理缺失key的情况
                item = Dict(json.loads(item))
                cmd = """INSERT INTO douban 
                         (movie_name, movie_type, movie_year, movie_rate)
                         VALUES (%s, %s, %s, %s);"""
                items = (item['movie_name'], item['movie_type'], 
                         item['movie_year'], item['movie_rate'])
                db.insert(cmd, items)
            else:
                break

    yield [enqueue(), dequeue()]


class Dict(dict):
    def __missing__(self, key):
        return ''


if __name__ == "__main__":
    IOLoop.current().run_sync(main)
	
