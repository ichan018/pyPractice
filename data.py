#put all functions related to data here
#print("testing")
#import myMenu

thePwd = [1,7,6]#change from tuple to list

#NUM_OF_CHOICES = 3 #CHANGE ALL INSTANCES OF Max_NUM to NUm_OF_CHOICES
NUM_IN_PWD = 3 #change num_in_list to num_in_pwd

userList = []

#index = 0 #used for GetUserList()


class User:
    def __init__(self,userName,pwd):
        self.userName = userName;
        self.pwd = pwd;

    def GetUserName(self):
        return self.userName;
    def GetPwd(self):
        return self.pwd;

# MakeUserList() is called once, at beginning of program
# ensures modules work


#def MakeUserList():
 #   userList = [];

def GetUserList(index):
    if index < len(userList): return userList[index]
    else: return User("ERROR: DOES NOT EXIST", -1)

def GetRangeUserList():
    return len(userList)

def UserLoc(userName):
    for x in range(len(userList)):
        if (userList[x].GetUserName() == userName):
            return x;
    return -1;

def AppendUser(name):
    userList.append(name)

def StartMenu(theName):
    optionStart = 0
    while (optionStart < 1 or optionStart > 2):
        print("What would you like to do?")
        print("1: Get user name")
        print("2: Change Password")
        optionStart = int(input(""));
        if (optionStart == 1):
            print("User name is:")
            findLoc = int(UserLoc(theName))
            if findLoc >= 0:
                print(userList[findLoc].GetUserName() )
        elif optionStart == 2:
            print("To do: Change pwd");
        else:
            print("Invalid option. Try again.")

