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
def email(email,password):
    try:
        auth.sign_in_with_email_and_password(email,password)
        print("Successfully logged in")
    except:
        print("Invalid try again")

def signup(email,password):
        auth.create_user_with_email_and_password(email,password)

def loanout(ID,ISBN,Date):
    db.child("books").child(ISBN).update({"Loaned":"yes"})
    data = {"ID":ID,"ISBN":ISBN,"Date":Date}
    db.child("outLoan").child(ID).push(data)

def returnLoan(ID,ISBN,Date):
    db.child("books").child(ISBN).update({"Loaned":"no"})
    db.child("outLoan").child(ID).remove()

def viewloans():
    loans = db.child("outLoan").get()
    for person in loans.each():
        print(person.val())
        print(person.key())

def AddBook(ISBN,Title,Author,Catergory,Year,loaned):
    data = {"ISBN":ISBN,"Title":Title,"Author":Author,"Category":Catergory,"Year":Year,"Loaned":loaned}
    db.child("books").child(ISBN).push(data)

def AddStudent(ID,Name,Surname,email,password):
    data = {"ID":ID,"Name":Name,"Surname":Surname,"Email":email,"Password":password}
    db.child("students").child(ID).push(data)

def UpdateStudent(ID,Column,Change):
    db.child("students").child(ID).update({Column:Change})

def UpdateBooks(ISBN,Column,Change):
    db.child("books").child(ISBN).update({Column:Change})

def viewStudents():
    students = db.child("students").get()
    for person in students.each():
        print(person.val())
        print(person.key())

def viewBooks():
    books = db.child("books").get()
    for person in books.each():
        print(person.val())
        print(person.key())

def SearchBookISBN(ISBN):
    books  = db.child("books").get()
    for person in books.each():
        if person.val()["ISBN"] == ISBN:
            print(person.val())
            print(person.key())

def SearchStudentID(ID):
    students  = db.child("students").get()
    for person in students.each():
        if person.val()["ID"] == ID:
            print(person.val())
            print(person.key())

def deleteStudent(ID):
    db.child("students").child(ID).remove()

def deleteBook(ISBN):
    db.child("books").child(ISBN).remove()


def booksonloan():
    books = db.child("books").get()
    for person in books.each():
        if person.val()["Loaned"] =="yes":
            print(person.val())
            print(person.key())
