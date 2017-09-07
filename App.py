##CMPT Semester Project
##Author: David Siegel
##Version: 0.1

playerName = input("What is your name?")
print("Hello " + playerName + "! Welcome to Five Nights at Freddies!")
print("You are outside an abandoned house, late on Halloween night. You went there looking for your friends who ran off ahead of you.")
def giveInstruction():{
    print("Choose an action from the list bellow:")
    }
giveInstruction()
print("1. Shout your friends's names.")
x = eval(input("?"))
print("=================================================")

if (x == 1):
    print("You shout out 'Jonathan!!'")
    print("Andrew!!")
    print("'Where are you??'")
    print("...")
    print("...")
    print("...")
    print("You get no response...")
else:
    print("I'm sorry that's not an option.")
