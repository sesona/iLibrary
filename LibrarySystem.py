## import the pyrebase library
import pyrebase

## use the config variable from the Firebase as firebaseConfig dictionary
FirebaseConfig = { "apiKey": "AIzaSyBSYFWV5E7IexfLszmeyj50JaE9ueZ8moE",
    "authDomain": "library-system-7360c.firebaseapp.com",
    "databaseURL":"https://library-system-7360c-default-rtdb.firebaseio.com/",
    "projectId": "library-system-7360c",
    "storageBucket": "library-system-7360c.appspot.com",
    "messagingSenderId": "102182920013",
    "appId": "1:102182920013:web:eee0c4a7b1e9d9d74c6104",
    "measurementId": "G-BWJFD5JJT6"}

## initializing the firebaseConfig dictionary to the firebase variable
firebase = pyrebase.initialize_app(FirebaseConfig)

## initializing reference variable for the Realtime Database
db = firebase.database()
## initializing reference variable for the Firebase Authentication
auth = firebase.auth()
#Push data


#login
## email method that handles exceptions and checks whether, the email and password entered by the user is valid or not
def email(email,password):
    try:
        auth.sign_in_with_email_and_password(email,password)
        print("Successfully logged in")
    except:
        print("Invalid try again")

## the user creates an account by entering their valid email and password        
def signup(email,password):
        auth.create_user_with_email_and_password(email,password)

def loanout(ID,ISBN,Date):
    db.child("books").child(ISBN).update({"Loaned":"yes"})      ## checks if a book is loaned using the ISBN in the database and updates the user 
    data = {"ID":ID,"ISBN":ISBN,"Date":Date}                    ## the user ID, book ISBN and date is assigned to data variable
    db.child("outLoan").child(ID).push(data)                    ## returns the selected element, ID

def returnLoan(ID,ISBN):
    db.child("books").child(ISBN).update({"Loaned":"no"})       ## checks if a book is loaned using the ISBN in the database and updates the user 
    db.child("outLoan").child(ID).remove()                      ## the library admin removes the selected element, ID from the database

def viewloans():
    try:
        loans = db.child("outLoan").get()
        for person in loans.each():
            print(person.val())
            print(person.key())
    except:
        print("No loaned books")

def AddBook(ISBN,Title,Author,Catergory,Year):
    data = {"ISBN":ISBN,"Title":Title,"Author":Author,"Category":Catergory,"Year":Year}     ## creates a dictionary consisting of all the book details and assigned to data variable
    db.child("books").child(ISBN).push(data)                                                ## returns all direct children of the books selected element, ISBN

def AddStudent(ID,Name,Surname,email,password):
    data = {"ID":ID,"Name":Name,"Surname":Surname,"Email":email,"Password":password}        ## creates a dictionary consisting of all the student details and assigned to data variable
    db.child("students").child(ID).push(data)                                               ## returns all direct children of the students selected element, ID

def UpdateStudent(ID,Column,Change):
    db.child("students").child(ID).update({Column:Change})                                  ## inserts a change to a students specific column

def UpdateBooks(ISBN,Column,Change):
    db.child("books").child(ISBN).update({Column:Change})                                   ## inserts a change to a books specific column

def viewStudents():
    try:
        students = db.child("students").get()
        for person in students.each():
            print(person.val())
            print(person.key())
    except:
        print("No Students in System")

def viewBooks():
    try:
        books = db.child("books").get()
        for person in books.each():
            print(person.val())
            print(person.key())
    except:
        print("No Books in System")

def SearchBookISBN(ISBN):
    pr = db.child("students").child(ISBN).get()
    print(pr.val())


def SearchStudentID(ID):
    pr = db.child("students").child(ID).get()
    print(pr.val())

def deleteStudent(ID):
    db.child("students").child(ID).remove()                     ## the library admin deletes the students selected element, ID from the database 

def deleteBook(ISBN):
    db.child("books").child(ISBN).remove()                      ## the library admin deletes the books selected element, ISBN from the database 

def myprofile(ID):
    pr = db.child("outLoan").child(ID).get()
    print(pr.val())


def booksonloan():
    books = db.child("books").get()                             ## the books variable is assigned to a database which returns the value for a given key, books
    for person in books.each():                                 ## iterates for person in the books variable for every matched key
        if person.val()["Loaned"] =="yes":
            print(person.val())                                 ## displays the value of the matched key
            print(person.key())                                 ## displays the list of all the matched key(s)



