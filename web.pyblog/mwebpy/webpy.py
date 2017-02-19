#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
from config import *
import web
import MySQLdb
import MySQLdb.cursors
  
urls = (

	'/article','article',
	'/blog/\d+','blog',
    '/(.*)', 'hello',
)
render = web.template.render('templates') 
app = web.application(urls, globals())

# class index:        
#     def GET(self):
#         query =web.input()
#         return query
class blog:        
    def GET(self):
    	return web.ctx.env
    def POST(self):
    	data = web.input()
    	return data




class hello:        
    def GET(self,name):
    	return render.hello2(name)

class article:        
    def GET(self):
    	conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass = MySQLdb.cursors.DictCursor)
    	cur =conn.cursor()
    	print conn
    	cur.execute("select * from mtianyan")
    	r = cur.fetchall()
    	cur.close()
    	conn.close()

    	print r
    	return render.article(r)

if __name__ == "__main__":
    app.run()