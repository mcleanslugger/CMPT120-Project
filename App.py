##CMPT Semester Project
##Author: David Siegel
##Version: 0.1

Command = ""
pLocation = ""
pName = input("What is your name? ")
pScore = 0
pStart              = ("You are in front of an abandoned house, late on Halloween night.You went there looking for your friends who ran off ahead of you.\n"
                       "You move to the front door and go inside. You walk into a dark, dingy main foyer. The door suddenly slams closed behind you...\n"
                       "You see a kitchen to your left, a dinning room to your right, and a long hallway with a window at the end in front of you...")

Kitchen             = ("You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces,\n"
                       "and there are no counters or cabinents anywhere.")
visitKitchen        = False
DinningRoom         = ("You walk into a dimly lit dinning room. The table is cracked in many places, and the chairs look like they haven't been\n"
                       "used in years.")
visitDinningRoom    = False
Window              = ("Window")
visitWindow         = False
FamilyRoom          = ("Family Room")
visitFamilyRoom     = False
Bathroom            = ("Bathroom")
visitBathroom       = False
LockDoor            = ("Locked Door")
visitLockDoor       = False

Ending              = ("You turn around to find a clown behind you. 'Hello " + pName + ", it's time to float.' the clown says laughing maniacally.\n"
                       "You try to run away but it grabs you and drags you downstairs...")


def startProgram():
    global pScore, pLocation, pStart
        
    print("Hello " + pName + "! Welcome to")
    print(" _____ _     _____           _     ___")
    print("|_   _| |   |  __ \         | |   |__ \ ")
    print("  | | | |_  | |__) |_ _ _ __| |_     ) |")
    print("  | | | __| |  ___/ _` | '__| __|   / / ")
    print(" _| |_| |_  | |  | (_| | |  | |_   / /_ ")
    print("|_____|\__| |_|   \__,_|_|   \__| |____|")
    print("\nBy: David Siegel")
    pLocation = pStart

def playGame():
    global Command, pScore, pStart, pLocation, Kitchen, DinningRoom, Window, FamilyRoom
    global Bathroom, LockDoor, visitKitchen, visitDinningRoom, visitWindow, visitFamilyRoom, visitBathroom, visitLockDoor

    print("\nYour score:", pScore)
    print("\n" + pLocation, "\n")
    print("=================================================\n")
    changeLocation()

def changeLocation():
    global Command, pScore, pStart, pLocation, Kitchen, DinningRoom, Window, FamilyRoom
    global Bathroom, LockDoor, visitKitchen, visitDinningRoom, visitWindow, visitFamilyRoom, visitBathroom, visitLockDoor
    Command = input("Please input a command: ")
    Command = Command.lower()
    
    print()
    while Command:
        if Command == 'help':
            print("List of commands:\nForward, Back, Right, Left, Help, Quit\n")
            print("=================================================\n")
            changeLocation()
        elif Command == 'quit':
            break

def EndGame():
    print(Ending)
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")



startProgram()
playGame()
if Command != 'quit':
    EndGame()

