from tkinter import *
from tkinter import messagebox 
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["database"]
collection = db["log"]

root = Tk()
root.title('Login')
instruction = Label(root, text='Enter your username and password\n')
instruction.grid(sticky=E)

unameL = Label(root, text='uname: ')
unameL.grid(row=1, sticky=W)
pwordL = Label(root, text='password: ')
pwordL.grid(row=2, sticky=W)

unameE = Entry(root)
unameE.grid(row=1, column=1, sticky=W)


pwordE = Entry(root, show='*')
pwordE.grid(row=2, column=1, sticky=W)


def message():
 for x in collection.find({},{"username","password"}):
  username=str(x["username"])
  password=str(x["password"])
 if unameE == username and pwordE == password:
     messagebox.showinfo("Information", "Login Successfull")
 else :
     messagebox.showinfo("Error", "Invalid Username or Password") 
     
loginButton = Button(root, text='Login',command = message)
loginButton.grid(columnspan=3, sticky=W)

root.mainloop()


