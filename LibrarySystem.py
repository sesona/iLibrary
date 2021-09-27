import pyrebase
from datetime import date
from collections import OrderedDict
import json


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
        print("Success! Sign up done!")
        return True
    except:
        print("Existing user or password incorrect!")
        return False

def checker(ID):
    OD = json.loads(json.dumps(SearchStudentID(ID)))
    if(OD == None):
        return False
    else:
        return True

def loanout(ID,ISBN): #Adds ID,ISBN and date into the loanout table
    try:
        time = date.today()
        time = time.strftime('%m/%d/%Y')
        data = {"ID":ID,"ISBN":ISBN,"Date":time}
        db.child("outLoan").child(ID).push(data)
    except:
        print("Error")

def returnLoan(ID,ISBN): #returns book back to book table and deletes entity
    try:
        db.child("outLoan").child(ID).remove()
    except:
        print("Error")

def AddBook(ISBN,Title,Author,Catergory,Year): #add book in books table
    data = {"ISBN":ISBN,"Title":Title,"Author":Author,"Category":Catergory,"Year":Year}
    db.child("books").child(ISBN).push(data)
    print(Title+" Has been Successfully added")

def AddStudent(ID,Name,Surname,email,password): #add students in students table
    if(checker(ID)==False):
        data = {"ID":ID,"Name":Name,"Surname":Surname,"Email":email,"Password":password}
        db.child("students").child(ID).push(data)
        print("User added to database")
        return True
    else:
        return False

def UpdateStudent(ID,Column,Change):
    db.child("students").child(ID).update({Column:Change})

def UpdateBooks(ISBN,Column,Change):
    OD = json.loads(json.dumps(SearchBookISBN(ISBN)))
    dict = []
    for i in OD:
        dict = OD[i]
    change =(dict["ISBN"])
    db.child("books").child(ISBN).update({Column:Change})

def viewStudents(): # view students
    keyID = []
    num = 0
    students = db.child("students").get()
    for person in students.each():
        keyID.append(int(person.key()))
    return(keyID)


def viewBooks(): #view books
    keyID = []
    num = 0
    books = db.child("books").get()
    for person in books.each():
        keyID.append(int(person.key()))
    return(keyID)

def viewloans():#checks the books that are onloan
    keyID = []
    ISBN = []
    num = 0
    loans = db.child("outLoan").get()
    for person in loans.each():
        keyID.append(int(person.key()))
        loaned = db.child("outLoan").child(keyID[num]).get()
        num = num+1
        loaned = loaned[0].val()
        ISBN.append(int(loaned["ISBN"]))
    return(keyID,ISBN)

def displayloans(keyID,ISBN):
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    stringhead =("{:<30} {:<30} {:<30} {:<30} {:<30}".format('ID','Email','ISBN','Title','Date'))
    for i in range(len(keyID)):
        Email,Name,ID,Password,Surname = splitStudent(keyID[i])
        ISBN,Title,Author,Catergory,Year = splitBook(ISBN[i])
        ID,ISBN,Date = splitOuts(keyID[i])
        stringhead = stringhead + "\n{:<30} {:<30} {:<30} {:<30} {:<30}".format(ID,Email,ISBN,Title,Date)
    return stringhead


def displaybooks(keyID):#allows the books to be viewed in a table
    stringhead = []
    #print each data item.
    for i in range(len(keyID)):
        ISBN,Title,Author,Catergory,Year = splitBook(keyID[i])
        stringhead.append([ISBN, Title, Author, Catergory, Year])
    df = pd.DataFrame(stringhead, columns =['ISBN', 'Title', 'Author', 'Category', 'Year'], dtype = int)
    return df.to_string(col_space = 20, max_colwidth = 60)

def displaystudents(keyID):#allows the students to be viewed in a table
    stringhead =("{:>40} {:>40} {:>40} {:>40} {:>40}".format('Email', 'ID', 'Name','Password','Surname'))
    stringhead = stringhead + (f"\n------------------------------------------------------------------------------")
#print each data item.
    for i in range(len(keyID)):
        Email,Name,ID,Password,Surname = splitStudent(keyID[i])
        stringhead = stringhead + "\n{:>40} {:>40} {:>40} {:>40} {:>40}".format(Email,ID,Name,Password,Surname)

    return stringhead

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

def SearchLoanID(ID): #search student by ID in student table
    try:
        pr = db.child("outLoan").child(ID).get()
        return(pr.val())
    except:
        print("Incorrect ID")

def deleteStudent(ID):# delete student
    db.child("students").child(ID).remove()

def deleteBook(ISBN):# delete book
    db.child("books").child(ISBN).remove()

def booksonloan():#checks the books that are onloan
    books = db.child("books").child("Loaned").get()
    return(books.val())


def splitStudent(ID): #Split the students attributes
    try:
        OD = json.loads(json.dumps(SearchStudentID(ID)))
        dict = []
        for i in OD:
            dict = OD[i]
        Email = (dict["Email"])
        Name = (dict["Name"])
        ID = (dict["ID"])
        Surname = (dict["Surname"])
        Password = (dict["Password"])
        return Email,Name,ID,Password,Surname
    except:
        print("ID does not exist")

def splitBook(ISBN):
    OD = json.loads(json.dumps(SearchBookISBN(ISBN)))
    dict = []
    for i in OD:
        dict = OD[i]
    uISBN = (dict["ISBN"])
    Author = (dict["Author"])
    Title = (dict["Title"])
    Catergory = (dict["Category"])
    Year = (dict["Year"])
    return uISBN,Title,Author,Catergory,Year

def splitOuts(ID):
    OD = json.loads(json.dumps(SearchLoanID(ID)))
    dict = []
    for i in OD:
        dict = OD[i]
    ID = (dict["ID"])
    ISBN = (dict["ISBN"])
    Date = (dict["Date"])
    return ID,ISBN,Date


def Field(ISBN,column):
    OD = json.loads(json.dumps(SearchBookISBN(ISBN)))
    dict = []
    for i in OD:
        dict = OD[i]
    field= dict[column]
    return field

def editBook(ISBN, column, change):
    OD = json.loads(json.dumps(SearchBookISBN(ISBN)))
    dict = []
    for i in OD:
        dict = OD[i]
    dict[column] = change

def SearchTitle(title):
    keyID = []
    keyID = viewBooks()
    Out = []
    for i in range(len(keyID)):
        if(Field(keyID[i],"Title") == title):
                ISBN,Title,Author,Catergory,Year = splitBook(keyID[i])
                Out.append(ISBN)
    return(Out)

def SearchCat(cat):
    keyID = []
    keyID = viewBooks()
    Out = []
    for i in range(len(keyID)):
        if(Field(keyID[i],"Category") == cat):
                ISBN,Title,Author,Catergory,Year = splitBook(keyID[i])
                Out.append(ISBN)
    return(Out)

def SearchYear(year):
    keyID = []
    keyID = viewBooks()
    Out = []
    for i in range(len(keyID)):
        if(Field(keyID[i],"Year") == year):
                ISBN,Title,Author,Catergory,Year = splitBook(keyID[i])
                Out.append(ISBN)
    return(Out)

def myprofile(ID): #Views my profile
    key = ID
    stringhead =("{:<30} {:<30} {:<30} {:<30} {:<30}".format('Email', 'ID', 'Name','Password','Surname',))
    Email,Name,ID,Password,Surname = splitStudent(key)
    stringhead = stringhead + "\n{:<30} {:<30} {:<30} {:<30} {:<30}".format(Email,ID,Name,Password,Surname)
    return(stringhead)

def mybooks(ID): #views my books
    try:
        key = ID
        ID,ISBN,Date = splitOuts(key)
        uISBN,Title,Author,Catergory,Year = splitBook(ISBN)
        stringhead =("{:<30} {:<30} {:<30} {:<30} {:<30}{:<30}".format('Title','ISBN','Author','Catergory','Year','Date'))
        stringhead = stringhead + "\n{:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format(Title,ISBN,Author,Catergory,Year,Date)
        return stringhead
    except:
        return(False)

#def checkUSER(gmail,password):
    # if((gmail =="adminILibrary@gmail.com" )&&(password=="123456789")):

