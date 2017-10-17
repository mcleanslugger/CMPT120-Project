##CMPT Semester Project
##Author: David Siegel
##Version: 0.5

Command = ""
pLocation = ""
pName = input("What is your name? ")
pScore = 0

visitKitchen        = False

visitDinningRoom    = False

visitHallway        = False

visitFamilyRoom     = False

visitBathroom       = False

visitWindow         = False

endVar              = False


##Location List:
##pStart       is Location[0]
##Kitchen      is Location[1]
##DinningRoom  is Location[2]
##Hallway      is Locaiton[3]
##FamilyRoom   is Location[4]
##Bathroom     is Location[5]
##Window       is Location[6]
##Ending       is Location[7]

Location = ["You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...",
            "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces,\n and there are no counters or cabinents anywhere.", 
            "You walk into a dimly lit dinning room. The table is cracked in many places, and the chairs look like they haven't been\nused in years.", 
            "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls.\nYou see a family room to your left, a window in front of you, and a bathroom to your right.", 
            "You enter the family room. The only thing is in the room is a couch with a picture resting on it.\nUpon further inspection, the picture has been scratched out a replaced with " + pName + " written in blood.", 
            "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words\nwritten in the slime: Do you like to float " + pName + "?",
            "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it,\nand for a second you think you see something move...",
            "You hear shuffling behind you. You turn around to find a clown behind you. 'Hello " + pName + ", it's time to float.' the clown says laughing maniacally.\nYou try to run away but it grabs you and drags you downstairs..."]
            
##Shows introduction and starting location

def startProgram():
    global pScore, pLocation
        
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
    pLocation = Location[0]

def playGame():
    global Command, pScore, pLocation, Location
    global visitKitchen, visitDinningRoom, visitWindow, visitFamilyRoom, visitBathroom, visitLockDoor, endVar

    while endVar == False:
        print("\nYour score:", pScore,
              "\n" + pLocation + "\n")
        print("=================================================\n")
        changeLocation()
    else:
        print("\n" + pLocation + "\n")
        EndGame()

def changeLocation():
    global Command, pScore, pLocation, pName, visitKitchen, visitDinningRoom
    global visitHallway, visitFamilyRoom, visitBathroom, visitWindow, endVar
    
    Command = input("Please input a command: ")
    Command = Command.lower()
    
    print()
    if Command == 'help' or Command == 'forward' or Command == 'back' or Command == 'right' or Command == 'left':
        if Command == 'help':
            print("List of commands:\nForward, Back, Right, Left, Help, Quit\n")
            print("=================================================\n")
            changeLocation()
                
        if Command == 'forward':
            if pLocation == Location[0]:
                pLocation = Location[3]
                if visitHallway == False:
                    pScore += 5
                    visitHallway = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[3]:
                pLocation = Location[6]
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
            if pLocation == Location[1]:
                pLocation = Location[0]
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[2]:
                pLocation = Location[0]
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[3]:
                pLocation = Location[0]
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[6]:
                pLocation = Location[3]
                if visitHallway == False:
                    pScore += 5
                    visitHallway = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[4]:
                pLocation = Location[3]
                if visitHallway == False:
                    pScore += 5
                    visitHallway = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[5]:
                pLocation = Location[3]
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
            if pLocation == Location[0]:
                pLocation = Location[2]
                if visitDinningRoom == False:
                    pScore += 5
                    visitDinningRoom = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[3]:
                pLocation = Location[5]
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
            if pLocation == Location[0]:
                pLocation = Location[1]
                if visitKitchen == False:
                    pScore += 5
                    visitKitchen = True
                if pScore == 30:
                    endVar = True
                playGame()
            elif pLocation == Location[3]:
                pLocation = Location[4]
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
    print(Location[7])
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")
    quit()


startProgram()
playGame()
