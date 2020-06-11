
"""
This file, given a name entered by the user and the current date, prints out a line of code with such information.
"""

import datetime
thePwd = (1,7,6)

#print("Hello world")
def check_pwd():
   
   currTuple = ();

   print("Enter 3 integers")
   for x in range(numInTuple):
       newTupleInput = int(input(""));

       newTuple = (newTupleInput,)
       currTuple = currTuple + newTuple

   print(currTuple);
  
   #compare tuples
   isPwd = 1
   for x in range(len(currTuple)):
       if currTuple[x] != thePwd[x]:
          isPwd = 0
       print(currTuple[x])
   return isPwd;
    


myName = input("Enter your name")

w = datetime.date.today();

myLine = "On {}, {} did something fun."

print(myLine.format(w, myName))

#numInTuple = int(input("How many values do you want in the tuple?"))
numInTuple = 3;


if check_pwd() == 1:
    print("Correct password")
else:
    print("Wrong password")
  


