
"""
This file, given a name entered by the user and the current date, prints out a line of code with such information.
"""

import datetime

#print("Hello world")

myName = input("Enter your name")

w = datetime.date.today();

myLine = "On {}, {} did something fun."

print(myLine.format(w, myName))

numInTuple = int(input("How many values do you want in the tuple?"))

print(numInTuple) #print for debugging

currTuple = ();
for x in range(numInTuple):
    newTupleInput = input("Enter new input");

    newTuple = (newTupleInput,)
    currTuple = currTuple + newTuple

print(currTuple)
