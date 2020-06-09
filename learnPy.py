import datetime

print("Hello world")

myName = input("Enter your name")

w = datetime.date.today();

myLine = "On {}, {} did something fun."

print(myLine.format(w, myName))
