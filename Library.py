import mysql.connector

db = mysql.connector.connect( ### this information is my mysql info to log into that server, should make your own server account
	host = "localhost",
	user = "root",
	passwd = "tKeZ!123",
	database = "books"
	)

mycursor = db.cursor()
#mycursor.execute("CREATE TABLE books(ISBM varchar(50) PRIMARY KEY , Title varchar(50), Author varchar(200), Category varchar(100), Year integer)")
#mycursor.execute("CREATE TABLE students(ID integer PRIMARY KEY, Name varchar(100),Surname varchar(100),Email varchar(20))")

def addbooks(ISBM,Title,Author,Category,Year):
	query = """INSERT INTO books (ISBM,Title,Author,Category,Year) VALUES (%s, %s,%s,%s,%s)"""
	## storing values in a variable
	values = (ISBM,Title,Author,Category,Year)
	## executing the query with values
	mycursor.execute(query, values)
	## to make final output we have to run the 'commit()' method of the database object
	db.commit()
	print("added")

def displaybooks ():
	query = "SELECT * FROM books"
	## getting records from the table
	mycursor.execute(query)
	## fetching all records from the 'cursor' object
	records = mycursor.fetchall()
	## Showing the data
	for record in records:
    		print(record)

def displaystudents ():
	query = "SELECT * FROM students"
	## getting records from the table
	mycursor.execute(query)
	## fetching all records from the 'cursor' object
	records = mycursor.fetchall()
	## Showing the data
	for record in records:
    		print(record)

def addstudents(ID,Name,Surname,Email):
	query = """INSERT INTO students (ID,Name,Surname,Email) VALUES (%s, %s,%s,%s)"""
	## storing values in a variable
	values = (ID,Name,Surname,Email)
	## executing the query with values
	mycursor.execute(query, values)
	## to make final output we have to run the 'commit()' method of the database object
	db.commit()
	print("added")



displaybooks()
addstudents(2,"Ricardo","Jeremy","myemail@gmail.com")
displaystudents()
