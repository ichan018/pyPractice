
"""
This file, given a name entered by the user and the current date, prints out a line of code with such information.
"""

import datetime
thePwd = [1,7,6]#change from tuple to list

MAX_NUM = 3
numInList = 3

#print("Hello world")
def check_pwd():
   
   currList = [];

   print("Enter 3 integers")
   for x in range(numInList): currList.append(int(input("")))
  
   #compare tuples
   isPwd = 1
   for x in range(len(currList)):
       if (currList[x] != thePwd[x]): isPwd = 0
   return isPwd;
    
def EnterPwd(): #FIX INDENTATION!
    myName = input("Enter your name")

    #w = datetime.date.today();
    # myLine = "On {}, {} did something fun."
    #print(myLine.format(w, myName))

    #numInTuple = int(input("How many values do you want in the tuple?"))
    #numInTuple = 3;

    if check_pwd() == 1: print("Correct password")
    else: print("Wrong password")


#begin program
#begin continuous loop
ifContinue = 1
while (ifContinue == 1):
    ifContinue = -1
    #ifContInput = "@";

    loginVal = -2
    while (not(loginVal >= -1 and (loginVal + 2) <= MAX_NUM)):
        print("Welcome to Ivan's Server. What would you like to do?")
        print("-1: Exit")
        print("0. Login")
        print("1.Add user") #ADD FUNCTIONALITY LATER
        loginVal = int(input(""))
   
    if(loginVal == -1): ifContinue = 0;
    #begin if loop
    if(ifContinue == -1): #program not ended by user pressing exit key
        if (loginVal == 0): EnterPwd();
        elif(loginVal == 1):
            print("Creation of part2 in progress")
            print("Checkin later")
        #end of while function

        #checkifcontinue (fix)
        #Create variable for testing continue
        while(not(ifContinue == 1 or ifContinue == 0)):
           ifContinue = int(input("Do you want to continue (yes = '1', no = '0')?"))
       #end if loop
