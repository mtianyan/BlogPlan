#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
from flask import *
import warnings
warnings.filterwarnings("ignore")
import MySQLdb
import MySQLdb.cursors
from config import *
import time

app = Flask(__name__)
app.config.from_object(__name__)


# 连接数据库
def connectdb():
	db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass = MySQLdb.cursors.DictCursor)
	print db;
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()

# 首页
@app.route('/')
def index():
	return render_template('index.html')

#文章列表
#
@app.route('/listpage')
def listpage():
	(db,cursor) = connectdb()
	cursor.execute("select * from mtianyan")
	data = cursor.fetchall()
	for x in xrange(0,len(data)):
		data[x]['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(data[x]['timestamp'])))



	closedb(db,cursor)
	return render_template('listpage.html',data = data);
#文章内容
#
@app.route('/postpage/<postpage_id>')
def postpage(postpage_id):
	(db,cursor) = connectdb()
	cursor.execute("select * from mtianyan where id=%s",[postpage_id])
	data = cursor.fetchone()
	data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(data['timestamp'])))


	return render_template('postpage.html',data=data);
#处理提交
@app.route('/handle', methods=['POST'])
def handle():
	data = request.form
	print data
	(db,cursor) = connectdb()
	cursor.execute("insert into mtianyan(title, content, timestamp) values(%s , %s, %s)", [data['title'], data['content'],int(time.time())])
	closedb(db,cursor)
	return redirect(url_for('listpage'))


if __name__ == '__main__':
	app.run(debug=True)