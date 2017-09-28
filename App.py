##CMPT Semester Project
##Author: David Siegel
##Version: 0.3

Command = ""
pLocation = ""
pName = input("What is your name? ")
pScore = 0
pStart              = ("You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...")

Kitchen             = ("You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces,\n"
                       "and there are no counters or cabinents anywhere.")
visitKitchen        = False
DinningRoom         = ("You walk into a dimly lit dinning room. The table is cracked in many places, and the chairs look like they haven't been\n"
                       "used in years.")
visitDinningRoom    = False
Hallway             = ("You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls.\n"
                       "You see a family room to your left, a window in front of you, and a bathroom to your right.")
visitHallway        = False
FamilyRoom          = ("You enter the family room. The only thing is in the room is a couch with a picture resting on it.\n"
                       "Upon further inspection, the picture has been scratched out a replaced with " + pName + " written in blood.")
visitFamilyRoom     = False
Bathroom            = ("You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words\n"
                       "written in the slime: Do you like to float " + pName + "?")
visitBathroom       = False
Window              = ("You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it,\n"
                       "and for a second you think you see something move...")
visitWindow         = False

Ending              = ("You hear shuffling behind you. You turn around to find a clown behind you. 'Hello " + pName + ", it's time to float.' the clown says laughing maniacally.\n"
                       "You try to run away but it grabs you and drags you downstairs...")
endVar              = False


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
    print("You are in front of an abandoned house, late on Halloween night.You went there looking for your friends who ran off ahead of you.\n"
          "You move to the front door and go inside. You walk inside and the door suddenly slams closed behind you...\n")
    input("Press a key to continue")
    pLocation = pStart

def playGame():
    global Command, pScore, pStart, pLocation, Kitchen, DinningRoom, Window, FamilyRoom
    global Bathroom, LockDoor, visitKitchen, visitDinningRoom, visitWindow, visitFamilyRoom, visitBathroom, visitLockDoor, endVar

    while endVar == False:
        print("\nYour score:", pScore,
              "\n" + pLocation + "\n")
        print("=================================================\n")
        changeLocation()
    else:
        print("\n" + pLocation + "\n")
        EndGame()

def changeLocation():
    global Command, pScore, pLocation, pName, pStart, Kitchen, visitKitchen, DinningRoom, visitDinningRoom
    global Hallway, visitHallway, FamilyRoom, visitFamilyRoom, Bathroom, visitBathroom, Window, visitWindow, endVar
    
    Command = input("Please input a command: ")
    Command = Command.lower()
    
    print()
    if Command == 'help' or Command == 'forward' or Command == 'back' or Command == 'right' or Command == 'left':
        if Command == 'help':
            print("List of commands:\nForward, Back, Right, Left, Help, Quit\n")
            print("=================================================\n")
            changeLocation()
                
        if Command == 'forward':
            if pLocation == pStart:
                pLocation = Hallway
                if visitHallway == False:
                    pScore += 5
                    visitHallway = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Hallway:
                pLocation = Window
                if visitWindow == False:
                    pScore += 5
                    visitWindow = True
                if pScore == 30:
                    endVar = True
                playGame()
            else:
                if pScore != 30:
                    print("Oops. There's a wall in the way. Try again.")
                    changeLocation()
                
        if Command == 'back':
            if pLocation == Kitchen:
                pLocation = pStart
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == DinningRoom:
                pLocation = pStart
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Hallway:
                pLocation = pStart
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Window:
                pLocation = Hallway
                if visitHallway == False:
                    pScore += 5
                    visitHallway = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == FamilyRoom:
                pLocation = Hallway
                if visitHallway == False:
                    pScore += 5
                    visitHallway = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Bathroom:
                pLocation = Hallway
                if visitHallway == False:
                    pScore += 5
                    visitHallway = True
                if pScore == 30:
                    endVar = True
                playGame()
            else:
                if pScore != 30:
                    print("Oops. There's a wall in the way. Try again.")
                    changeLocation()
                
        if Command == 'right':
            if pLocation == pStart:
                pLocation = DinningRoom
                if visitDinningRoom == False:
                    pScore += 5
                    visitDinningRoom = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Hallway:
                pLocation = Bathroom
                if visitBathroom == False:
                    pScore += 5
                    visitBathroom = True
                if pScore == 30:
                    endVar = True
                playGame()
            else:
                if pScore != 30:
                    print("Oops. There's a wall in the way. Try again.")
                    changeLocation()
                
        if Command == 'left':
            if pLocation == pStart:
                pLocation = Kitchen
                if visitKitchen == False:
                    pScore += 5
                    visitKitchen = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Hallway:
                pLocation = FamilyRoom
                if visitFamilyRoom == False:
                    pScore += 5
                    visitFamilyRoom = True
                if pScore == 30:
                    endVar = True
                playGame()
            else:
                if pScore != 30:
                    print("Oops. There's a wall in the way. Try again.")
                    changeLocation()
    elif Command == 'quit':
        quit()
    else:
        print("Please input a valid command, or type 'help' to view a list of valid commands.")
        print("=================================================\n")
        changeLocation()
        

def EndGame():
    print(Ending)
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")
    quit()


startProgram()
playGame()
