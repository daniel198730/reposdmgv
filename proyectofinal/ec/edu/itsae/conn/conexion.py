'''
Created on 19/2/2015

@author: PC29
'''

from flaskext.mysql import MySQL
from flask import Flask

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'venta'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'ventas'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


con=mysql.connect().cursor()
con.execute(" select * from alumno" )
report=con.fetchall()
print report 
