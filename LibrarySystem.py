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

def AddBook(ISBN,Title,Author,Catergory,Year):
    data = {"ISBN":ISBN,"Title":Title,"Author":Author,"Category":Catergory,"Year":Year}
    db.child("books").push(data)

def AddStudent(ID,Name,Surname,email,password):
    data = {"ID":ID,"Name":Name,"Surname":Surname,"Email":email,"Password":password}
    db.child("students").push(data)

def UpdateStudent(Column,Change):
    db.child("students").update({Column:Change})

def UpdateBooks(Column,Change):
    db.child("books").update({Column:Change})

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

def SearchBook(ISBN):
    books  = db.child("books").get()
    for person in books.each():
        if person.val()["ISBN"] == ISBN:
            print(person.val())
            print(person.key())
