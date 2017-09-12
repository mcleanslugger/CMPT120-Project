##CMPT Semester Project
##Author: David Siegel
##Version: 0.1

import math
playerName = input("What is your name?")
print("Hello " + playerName + "! Welcome to Five Nights at Freddies!")
playerLocation = "You are outside an abandoned house, late on Halloween night. You went there looking for your friends who ran off ahead of you."
print(playerLocation)
def giveInstruction():{
    print("Please press enter")
    }
giveInstruction()
print("1. Shout your friends's names.")
x = int(input("?"))
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
