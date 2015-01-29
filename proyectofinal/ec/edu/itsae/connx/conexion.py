'''
Created on 29/1/2015

@author: PERSONAL
'''


from flaskext.mysql import MySQL
from flask import Flask

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'edwinagua'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app.config['MYSQL_DATABASE_DB'] = 'compras'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


con=mysql.connect().cursor()
con.execute(" select * from producto ")
report=con.fetchall()
print report
