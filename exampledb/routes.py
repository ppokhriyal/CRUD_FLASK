from flask import render_template, url_for, flash, redirect, request, abort, session,jsonify
from exampledb import app,mysql
from flask_mysqldb import MySQL,MySQLdb
import json

@app.route('/')
def index():
	try:
		cur = mysql.connection.cursor()
		cur.execute('''CREATE TABLE employee (empid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20) NOT NULL,dept VARCHAR(20) NOT NULL)''')

	except MySQLdb._exceptions.OperationalError :
		print ("Database Already available")
		#Fetch All the Data from Database
		cur.execute('''SELECT * FROM employee''')
		data = cur.fetchall()
		cur.close()
		print(json.dumps(data))
	return render_template('home.html',empdata=data)


@app.route('/add',methods=['POST'])
def add_emp_data():
	
	empname = request.form['empname']
	empdpt = request.form['empdpt']

	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO employee (name,dept) VALUES (%s,%s)",(empname,empdpt))
	mysql.connection.commit()

	return redirect(url_for('index'))

@app.route('/delete/<string:id_data>',methods=['GET'])
def del_emp_data(id_data):

	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM employee WHERE empid=%s",(id_data,))
	mysql.connection.commit()

	return redirect(url_for('index'))