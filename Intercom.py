#!/usr/bin/python

# import the MySQLdb and sys modules
import MySQLdb
import sys

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "192.168.1.2", user = "user", passwd = "password", db = "user")

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute the SQL query using execute() method.
cursor.execute ("select id, name, email from user")

# fetch all of the rows from the query
try:
	data = cursor.fetchall()
except:
	print("Error getting user data.")

# print the rows
for row in data :
	Id = row[0]
	Name = row[1]
	email = row[2]

	# API for intercom to insert user to intercom database
	try:
		intercomAPIInsert(name, email)
	except:
		print("Error inserting into intelcom.")

# close the cursor object
cursor.close()

# close the connection
connection.close()

# exit the program
sys.exit()
