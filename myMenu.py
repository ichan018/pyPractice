

#This file, given a name entered by the user and the current date, prints out a line of code with such information
from data import User, UserLoc, StartMenu, GetUserList, GetRangeUserList, AppendUser


#from tkinter import *
from doctest import testmod

import datetime

NUM_OF_CHOICES = 3;


# BEGIN COMMENT HERE

#thePwd = [1,7,6]#change from tuple to list
#
#NUM_OF_CHOICES = 3 #CHANGE ALL INSTANCES OF Max_NUM to NUm_OF_CHOICES
#NUM_IN_PWD = 3 #change num_in_list to num_in_pwd
#
#userList = []
#
#
#
#class User:
#    def __init__(self,userName,pwd):
#        self.userName = userName;
#        self.pwd = pwd;
#
#    def GetUserName(self):
#        return self.userName;
#    def GetPwd(self):
#        return self.pwd;
#
#    def UserLoc(userName):
#    for x in range(len(userList)):
#        if (userList[x].GetUserName() == userName):
#            return x;
#    return -1;

# END COMMENT HERE


#print("Hello world")
#def check_pwd(myName, myPwd):
def check_info(myName, myPwd):

   #check if user isn't here
   isPwd = -1
   isHere = 0
   #for x in range(len(userList)):
   for x in range(GetRangeUserList()): 
    #print("Hi. Add user first");
       #if((userList[x].GetUserName()== myName) and (userList[x].GetPwd() == myPwd)):
       #if((GetUserList(x).GetUserName() == myName) and (GetUserList(x).GetPwd() == myPwd)):
       if(GetUserList(x).GetUserName() == myName):
           if(GetUserList(x).GetPwd() == myPwd): 
               isPwd = 2
           else:
               isPwd = 1 # wrong password
       else:
           isPwd = 0;
   
   
   #print("make check pwd function after userList is read")
   return isPwd;
    
def UserLogin(): #FIX INDENTATION!
    myName = input("Enter your name:")

    #myPwd = int(input("Enter integer password:"))
    myPwd = input("Enter password") #allow pwd with chars

    if check_info(myName, myPwd) == 2: 
        print("Correct password")
        StartMenu(myName)
    elif check_info(myName,myPwd) == 1:
        print("Wrong password, try again")
    else: 
        print("User not found, try again")

def AddUser():
    #add userName
    newUserName = input("Enter username: ");
    #newPwd = int(input("Enter an integer password: "));
    newPwd = input("Enter a password: ")

    newUser = User(newUserName, newPwd)

    #newPwd = int(input("Enter an integer password: "));
    # CREATE FUNCTION APPEND
    AppendUser(newUser)


#begin program
#begin continuous loop
#MakeUserList(); # creates user list

ifContinue = 1
while (ifContinue == 1):
    #ifContinue = -1
    #ifContInput = "@";

    loginVal = -2
    while (not(loginVal >= -1 and (loginVal + 2) <= NUM_OF_CHOICES)):
        print("Welcome to Ivan's Server. What would you like to do?")
        print("-1: Exit")
        print("0. Login")
        print("1.Add user") #ADD FUNCTIONALITY LATER
        loginVal = int(input(""))
   
    if(loginVal == -1): ifContinue = 0;

    #begin if loop
    if(ifContinue == 1): #program not ended by user pressing exit key
        if (loginVal == 0): UserLogin();
        elif(loginVal == 1):AddUser();
        elif(loginVal == -1): ifContinue = 0
        #end of while function

        #checkifcontinue (fix)
        #Create variable for testing continue
        #while(not(ifContinue == 1 or ifContinue == 0)):
           #ifContinue = int(input("Do you want to continue (yes = '1', no = '0')?"))
       #end if loop
