import pyrebase
from datetime import date


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

def loanout(ID,ISBN): #Adds ID,ISBN and date into the loanout table
    try:
        db.child("books").child(ISBN).update({"Loaned":"yes"})
        time = date.today()
        time = time.strftime('%m/%d/%Y')
        data = {"ID":ID,"ISBN":ISBN,"Date":time}
        db.child("outLoan").child(ID).push(data)
    except:
        print("Error")

def returnLoan(ID,ISBN): #returns book back to book table and deletes entity
    try:
        db.child("books").child(ISBN).update({"Loaned":"no"})
        db.child("outLoan").child(ID).remove()
    except:
        print("Error")

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
    keyID = []
    num = 0
    students = db.child("students").get()
    for person in students.each():
        keyID.append(int(person.key()))
    return(KeyID)

def viewBooks(): #view books
    try:
        books = db.child("books").get()
        for person in books.each():
            print(person.val())
            print(person.key())
    except:
        print("No Books in System")

def SearchBookISBN(ISBN): #search book by ISBN in books table
    try:
        pr = db.child("books").child(ISBN).get()
        return(pr.val())
    except:
        print("Incorrect ISBN")

def SearchStudentID(ID): #search student by ID in student table
    try:
        pr = db.child("students").child(ID).get()
        return(pr.val())
    except:
        print("Incorrect ID")

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


def splitStudent(ID): #Split the students attributes
    try:
        pr = db.child("students").child(ID).get()
        pr = (pr[0].val())
        Email = (pr["Email"])
        Name = (pr["Name"])
        ID = (pr["ID"])
        Surname = (pr["Surname"])
        Password = (pr["Password"])
        return Email,Name,ID,Password,Surname
    except:
        print("ID does not exist")


def splitBook(ISBN): #Split the students attributes
    try:
        pr = db.child("books").child(ISBN).get()
        pr = (pr[0].val())
        ISBN = (pr["ISBN"])
        print()
        Title = (pr["Title"])
        Catergory = (pr["Category"])
        Year = (pr["Year"])
        return ISBN,Title,Catergory,Year
    except:
        print("ISBN does not exist")




#print ("{:<30} {:<30} {:<30} {:<30} {:<30}".format('Email', 'ID', 'Name','Password','Surname'))
# print each data item.
#for i in range(len(keyID)):
    #Email,Name,ID,Password,Surname = split(keyID[i])
    #print("{:<30} {:<30} {:<30} {:<30} {:<30}".format(Email,ID, Name,Password,Surname))
