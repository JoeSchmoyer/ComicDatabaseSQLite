# Inorder to use MySQL for the flask database you first need a MySQL server then run this file to create the database
# Using mysql connector to make SQL queries through python
import mysql.connector

# Connect to MySQL Server using native password (needed for flask app configuration)
db = mysql.connector.connect(host='localhost', user='root', passwd='passw0rd', auth_plugin='mysql_native_password')
cursor = db.cursor()

# Creates the database (WARNING ONLY RUN ONCE OR ELSE IT WILL CLEAR THE DATABASE)
# cursor.execute("CREATE DATABASE ComicBase")
# Print databases on server
cursor.execute("SHOW DATABASES")
for dbs in cursor:
    print(dbs)
