import pyrebase

FirebaseConfig = { "apiKey": "AIzaSyBSYFWV5E7IexfLszmeyj50JaE9ueZ8moE",
    "authDomain": "library-system-7360c.firebaseapp.com",
    "databaseURL":"https://library-system-7360c-default-rtdb.firebaseio.com/",
    "projectId": "library-system-7360c",
    "storageBucket": "library-system-7360c.appspot.com",
    "messagingSenderId": "102182920013",
    "appId": "1:102182920013:web:eee0c4a7b1e9d9d74c6104",
    "measurementId": "G-BWJFD5JJT6"}


firebase = pyrebase.initialize_app(FirebaseConfig)

db = firebase.database()
auth = firebase.auth()
#Push data


#login
def email(email,password): #email login 
    try:
        auth.sign_in_with_email_and_password(email,password)
        print("Successfully logged in")
    except:
        print("Invalid try again")

def signup(email,password): #sign up
    try:
        auth.create_user_with_email_and_password(email,password)
    except:
        print("Password too short")

def loanout(ID,ISBN,Date): #Adds ID,ISBN and date into the loanout table
    db.child("books").child(ISBN).update({"Loaned":"yes"})
    data = {"ID":ID,"ISBN":ISBN,"Date":Date}
    db.child("outLoan").child(ID).push(data)

def returnLoan(ID,ISBN): #returns book back to book table and deletes entity
    db.child("books").child(ISBN).update({"Loaned":"no"})
    db.child("outLoan").child(ID).remove()

def viewloans():
    try:
        loans = db.child("outLoan").get()
        for person in loans.each():
            print(person.val())
            print(person.key())
    except:
        print("No loaned books")

def AddBook(ISBN,Title,Author,Catergory,Year): #add book in books table
    data = {"ISBN":ISBN,"Title":Title,"Author":Author,"Category":Catergory,"Year":Year}
    db.child("books").child(ISBN).push(data)
    print(Title+" Has been Successfully added")

def AddStudent(ID,Name,Surname,email,password): #add students in students table
    data = {"ID":ID,"Name":Name,"Surname":Surname,"Email":email,"Password":password}
    db.child("students").child(ID).push(data)

def UpdateStudent(ID,Column,Change):
    db.child("students").child(ID).update({Column:Change})

def UpdateBooks(ISBN,Column,Change):
    db.child("books").child(ISBN).update({Column:Change})

def viewStudents(): # view students
    try:
        students = db.child("students").get()
        for person in students.each():
            print(person.val())
            print(person.key())
    except:
        print("No Students in System")

def viewBooks(): #view books
    try:
        books = db.child("books").get()
        for person in books.each():
            print(person.val())
            print(person.key())
    except:
        print("No Books in System")

def SearchBookISBN(ISBN): #search book by ISBN in books table
    pr = db.child("students").child(ISBN).get()
    return(pr.val())

def SearchStudentID(ID): #search student by ID in student table
    pr = db.child("students").child(ID).get()
    return(pr.val())

def deleteStudent(ID):# delete student
    db.child("students").child(ID).remove()

def deleteBook(ISBN):# delete book
    db.child("books").child(ISBN).remove()

def myprofile(ID): #Views my profile 
    pr = db.child("outLoan").child(ID).get()
    return(pr.val())


def booksonloan():
    books = db.child("books").child("Loaned").get()
    print(books.val())


def split(ID): #Split the students attributes
    pr = db.child("students").child(ID).get()
    pr = (pr[0].val())
    Email = (pr["Email"])
    Name = (pr["Name"])
    ID = (pr["ID"])
    Password = (pr["Password"])
    print(pr.val())

    return Email,Name,ID,Password



