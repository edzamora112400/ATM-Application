import tkinter as tk
from tkinter import *
import sys

global userInput 
global passInput
global amount1

print("**************************    A T M   M A C H I N E   ******************************")
print("Hello, this is a simple ATM application.")
print("Below you can track the amount of money in your account, starting at $1,000.")

userInput = "Username"
passInput = "Password"

Balance = open("funds.txt", "r")
amount1 = Balance.read()
Balance.close()
print("Your Balance is: $" + amount1)


def destroyBox():
    notenough.destroy()

def notEnoughFunds():
    global notenough
    notenough = Toplevel(accountScreen)
    notenough.title("INFO BOX")
    notenough.geometry("170x100")
    notenough.resizable(0, 0)
    message = Label(notenough, text = "You don't have enough funds\nto withdraw",
                    fg = "blue").pack()
    Button(notenough, text = "OK", command = destroyBox, bg = "red", fg = "white",
           width = "6", height = "2").pack(padx = 5, pady = 5)
    

def allOfYourFunds():
    allOfYourFunds = Tk()
    allOfYourFunds = Label(withdrawScreen, text = "You are withdrawing all of the funds in this\naccount",
                           fg = "red")
    allOfYourFunds.pack()

def twenty():
    global amount1
    global newAmount
    
    Balance = open("funds.txt", "r")
    amount1 = Balance.read()
    amount2 = int(amount1)
    if amount2 <= 20:
        notEnoughFunds()
        Balance.close()
    else:
        Balance = open("funds.txt", "w")
        newAmount = str(amount2 - 20)
        edit = Balance.write(newAmount)
        Balance.close()
        print("Your balance is now: $" + newAmount)

def forty():
    global amount1
    global newAmount
    
    Balance = open("funds.txt", "r")
    amount1 = Balance.read()
    amount2 = int(amount1)
    if amount2 <= 40:
        notEnoughFunds()
        Balance.close()
    else:
        Balance = open("funds.txt", "w")
        newAmount = str(amount2 - 40)
        edit = Balance.write(newAmount)
        Balance.close()
        print("Your balance is now: $" + newAmount)

def sixty():
    global amount1
    global newAmount
    
    Balance = open("funds.txt", "r")
    amount1 = Balance.read()
    amount2 = int(amount1)
    if amount2 <= 60:
        notEnoughFunds()
        Balance.close()
    else:
        Balance = open("funds.txt", "w")
        newAmount = str(amount2 - 60)
        edit = Balance.write(newAmount)
        Balance.close()
        print("Your balance is now: $" + newAmount)

def eighty():
    global amount1
    global newAmount
    
    Balance = open("funds.txt", "r")
    amount1 = Balance.read()
    amount2 = int(amount1)
    if amount2 <= 80:
        notEnoughFunds()
        Balance.close()
    else:
        Balance = open("funds.txt", "w")
        newAmount = str(amount2 - 80)
        edit = Balance.write(newAmount)
        Balance.close()
        print("Your balance is now: $" + newAmount)

def onehundred():
    global amount1
    global newAmount
    
    Balance = open("funds.txt", "r")
    amount1 = Balance.read()
    amount2 = int(amount1)
    if amount2 <= 100:
        notEnoughFunds()
        Balance.close()
    else:
        Balance = open("funds.txt", "w")
        newAmount = str(amount2 - 100)
        edit = Balance.write(newAmount)
        Balance.close()
        print("Your balance is now: $" + newAmount)

def messageAndWithdraw():
    withdrawMessage.destroy()
    otherScreen.destroy()

def withdrawMessage():
    global withdrawMessage
    withdrawMessage = Toplevel(withdrawScreen)
    withdrawMessage.title("Success")
    withdrawMessage.geometry("180x100")
    withdrawMessage.resizable(0, 0)
    Label(withdrawMessage, text = "The widraw was successful!", fg = "green").pack()
    Button(withdrawMessage, text = "Ok", bg = "green", width = 10,
           height = 2, command = messageAndWithdraw).pack(padx = 5, pady = 5)

def withdrawAmount():
    entry = amountEntry.get()
    newentry = int(entry)
    Balance = open("funds.txt", "r")
    amount1 = Balance.read()
    amount2 = int(amount1)
        
    if amount2 <= newentry:
        notEnoughFunds()
        Balance.close()
    else:
        Balance = open("funds.txt", "w")
        newAmount = str(amount2 - newentry)
        edit = Balance.write(newAmount)
        Balance.close()
        print("Your balance is now: $" + newAmount)

    withdrawMessage()

def messageAndDeposit():
    depositmessage.destroy()
    depositScreen.destroy()

def depositMessage():
    global depositmessage
    depositmessage = Toplevel(depositScreen)
    depositmessage.title("Success")
    depositmessage.geometry("180x100")
    depositmessage.resizable(0, 0)
    Label(depositmessage, text = "The deposit was successful!", fg = "green").pack()
    Button(depositmessage, text = "Ok", bg = "green", width = 10,
           height = 2, command = messageAndDeposit).pack(padx = 5, pady = 5)
    
def depositAmount():
    entry = depositEntry.get()
    newentry = int(entry)
    Balance = open("funds.txt", "r")
    amount1 = Balance.read()
    amount2 = int(amount1)
    Balance = open("funds.txt", "w")
    newAmount = str(amount2 + newentry)
    edit = Balance.write(newAmount)
    Balance.close()
    depositMessage()
    print("Your balance is now: $" + newAmount)


def click(key):
    if len(amountEntry.get()) != 0:
         withdraw.configure(state = "active")

def click2(key):
    if len(depositEntry.get()) != 0:
         deposit.configure(state = "active")
    
def other():
    global otherScreen
    global amountEntry
    global withdraw
    
    otherScreen = Toplevel(accountScreen)
    otherScreen.title("Other Menu")
    otherScreen.geometry("225x160")
    otherScreen.resizable(0, 0)
    Label(otherScreen, text = "Enter the amount you wish to withdraw\nfrom your account :",
          fg = "red").pack()
    amountEntry = Entry(otherScreen, width = 15)
    amountEntry.pack()
    withdraw = Button(otherScreen, text = "Withdraw", bg = "red", fg = "white",
           command = withdrawAmount, state = "disabled")
    withdraw.pack(padx = 10, pady = 10)
    amountEntry.bind("<Key>", click)   

def exitDeposit():
    depositScreen.destroy()

def depositScreen():
    global depositEntry
    global depositScreen
    global deposit
    depositScreen = Toplevel(accountScreen)
    depositScreen.title("Deposit Menu")
    depositScreen.geometry("300x300")
    depositScreen.resizable(0, 0)
    Label(depositScreen, text = "Your account balance is: ", fg = "blue").pack()
    Label(depositScreen, text = amount1).pack()
    Label(depositScreen, text = "How much would you like to deposit into\nyour account?",
          fg = "blue").pack()
    depositEntry = Entry(depositScreen, width = 15)
    depositEntry.pack()
    deposit = Button(depositScreen, text = "Deposit", bg = "red", fg = "white",
           command = depositAmount, state = "disabled")
    deposit.pack(padx = 10, pady = 10)
    depositEntry.bind("<Key>", click2)
    Exit = Button(depositScreen, text = "Exit", width = "5", height = "2",
                      bg = "purple", fg = "white", command = exitDeposit)
    Exit.pack(padx = 10, pady = 2)

def Exit():
    withdrawScreen.destroy()

def withdrawScreen():
    global withdrawScreen
    withdrawScreen = Toplevel(accountScreen)
    withdrawScreen.title("Withdraw Menu")
    withdrawScreen.geometry("300x300")
    withdrawScreen.resizable(0, 0)
    Label(withdrawScreen, text = "Your account balance is: ", fg = "blue").pack()
    Label(withdrawScreen, text = amount1).pack()
    Label(withdrawScreen, text = "How much would you like to withdraw from\nyour account?",
          fg = "green").pack()
    btn1 = Button(withdrawScreen, text = "$20", width = "5", height = "2", bg = "red",
                  fg = "white", command = twenty)
    btn1.pack(padx = 10, pady = 2)
    btn1.place(x = 80, y = 100)
    
    btn2 = Button(withdrawScreen, text = "$40", width = "5", height = "2", bg = "red",
                  fg = "white", command = forty)
    btn2.pack(padx = 10, pady = 2)
    btn2.place(x = 130, y = 100) 
    
    btn3 = Button(withdrawScreen, text = "$60", width = "5", height = "2", bg = "red",
                  fg = "white", command = sixty)
    btn3.pack(padx = 10, pady = 2)
    btn3.place(x = 180, y = 100) 
    
    btn4 = Button(withdrawScreen, text = "$80", width = "5", height = "2", bg = "red",
                  fg = "white", command = eighty)
    btn4.pack(padx = 10, pady = 2)
    btn4.place(x = 80, y = 150) 
    
    btn5 = Button(withdrawScreen, text = "$100", width = "5", height = "2", bg = "red",
                  fg = "white", command = onehundred)
    btn5.pack(padx = 10, pady = 2)
    btn5.place(x = 130, y = 150)
    
    btn6 = Button(withdrawScreen, text = "Other", width = "5", height = "2", bg = "red",
                  fg = "white", command = other)
    btn6.pack(padx = 10, pady = 2)
    btn6.place(x = 180, y = 150)

    goToHome = Button(withdrawScreen, text = "Exit", width = "5", height = "2",
                      bg = "purple", fg = "white", command = Exit)
    goToHome.pack(padx = 10, pady = 2)
    goToHome.place(x = 130, y = 210)


def logOut():
    accountScreen.destroy()

def accountMenu():
    global accountScreen
    accountScreen = Toplevel(mainScreen)
    accountScreen.title("Home Page")
    accountScreen.geometry("300x300")
    accountScreen.resizable(0, 0)
    Label(accountScreen, text = "Hello, User!", bg = "purple", fg  = "white").pack(fill = tk.X)
    Label(accountScreen, text = "Your account balance is: ", fg = "blue").pack()
    Label(accountScreen, text = amount1).pack()
    Button(accountScreen, text = "Withdraw", bg = "red", fg = "white", width = "10",
           height = "2", command = withdrawScreen).pack(padx = 10, pady = 10)
    Button(accountScreen, text = "Deposit", bg = "green", fg = "white", width = "10",
           height = "2", command = depositScreen).pack(padx = 10, pady = 10)
    logOff = Button(accountScreen, text = "Log Out", bg = "purple", fg = "white",width = "10",
                    height = "2", command = logOut)
    logOff.pack(padx = 10, pady = 2)
    logOff.place(x = 110, y = 210)

def loginFail():
    fail = Label(mainScreen, text = 'Login Failed', fg = "red")
    fail.pack()
    mainScreen.after(2000, lambda : fail.config(text = ''))

def loginSuccess():
    success = Label(mainScreen, text = 'Successful Login', fg = "green")
    success.pack()
    mainScreen.after(2000, lambda : success.config(text = ''))

def clearEntry():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)

def verifySignIn():
    user = usernameEntry.get()
    paswrd = passwordEntry.get()

    verifyUser = userInput
    verifyPass = passInput

    if user == verifyUser and paswrd == verifyPass:
        loginSuccess()
        accountMenu()
        clearEntry()
    else:
        loginFail()
    
def mainScreen():
    global mainScreen
    global usernameEntry
    global passwordEntry
    
    mainScreen = Tk()
    mainScreen.title("Main Menu")
    mainScreen.geometry("300x300")
    mainScreen.resizable(0, 0)

    title = Label(text = "ATM", width = "10", height = "5", bg = "blue", fg = "white")
    title.pack(fill = tk.X, side = tk.TOP)

    frame = Frame(master = mainScreen, width = 200, height = 100)
    frame.pack

    username = Label(text = "Username")
    username.pack()

    usernameEntry = Entry(width = "25")
    usernameEntry.pack()

    password = Label(text = "Password")
    password.pack()

    passwordEntry = Entry(width = "25")
    passwordEntry.pack()

    signIn = Button(text = "Sign In", bg = "green", fg = "white", width = "10", height = "2",
                       command = verifySignIn)
    signIn.pack(padx = 10, pady = 10)

    mainScreen.mainloop()
    

mainScreen()
