from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = '878436c0a462c4145fa59eec2c43a66a'

#Configure Mysqldb
app.config['MYSQL_USER'] = 'sql12362497'
app.config['MYSQL_PASSWORD'] = 'YuGaPjW3MG'
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql12362497'

mysql = MySQL(app)

from exampledb import routes