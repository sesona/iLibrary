import mysql.connector


db = mysql.connector.connect( ### this information is my mysql info to log into that server
	host = "localhost",
	port = "3306",
	user = "root",
	passwd = "",
	database = "library system"
	)

mycursor = db.cursor()

def addBook(ISBN,Title,Author,Category,Year):
	query = """INSERT INTO books (ISBN,Title,Author,Category,Year) VALUES (%s, %s,%s,%s,%s)"""
	## storing values in a variable
	values = (ISBN,Title,Author,Category,Year)
	## executing the query with values
	mycursor.execute(query, values)
	## to make final output we have to run the 'commit()' method of the database object
	db.commit()
	print("added")

def delBook(ISBN):
	## executing the query
	mycursor.execute(f"DELETE FROM books WHERE ISBN = {ISBN}")
	## final step to tell the database that we have changed the table data
	db.commit()

def displayBooks ():
	query = "SELECT * FROM books"
	## getting records from the table
	mycursor.execute(query)
	## fetching all records from the 'cursor' object
	records = mycursor.fetchall()
	## Showing the data
	for record in records:
    		print(record)

def displayStudents ():
	query = "SELECT * FROM students"
	## getting records from the table
	mycursor.execute(query)
	## fetching all records from the 'cursor' object
	records = mycursor.fetchall()
	## Showing the data
	for record in records:
    		print(record)

def addStudent(ID,Name,Surname,Email,Password):
	query = """INSERT INTO students (ID,Name,Surname,Email,password) VALUES (%s, %s,%s,%s,%s)"""
	## storing values in a variable
	values = (ID,Name,Surname,Email,Password)
	## executing the query with values
	mycursor.execute(query, values)
	## to make final output we have to run the 'commit()' method of the database object
	db.commit()
	print("added")

def delStudent(num):
	## executing the query
	mycursor.execute(f"DELETE FROM students WHERE id = {num}")
	## final step to tell the database that we have changed the table data
	db.commit()


def searchBook(Y):
	
	## getting records from the table
	mycursor.execute(f"SELECT * FROM books WHERE Year= {Y}")
	## fetching all records from the 'cursor' object
	records = mycursor.fetchall()
	## Showing the data
	for record in records:
		print(record)

def updateBook(Title,ISBN):
	## executing the query
	mycursor.execute("UPDATE users SET name = (Title) WHERE id = {ISBN}")
	## final step to tell the database that we have changed the table data
	db.commit() 
