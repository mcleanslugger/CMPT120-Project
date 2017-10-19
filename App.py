##CMPT Semester Project
##Author: David Siegel
##Version: 0.5

Command = ""
pLocation = ""
pName = input("What is your name? ")
pScore = 0

                    ##Location List:
pStart = 0          ##pStart       is Location[0]
Kitchen = 1         ##Kitchen      is Location[1]
DiningRoom =2       ##DiningRoom   is Location[2]
Hallway = 3         ##Hallway      is Locaiton[3]
FamilyRoom = 4      ##FamilyRoom   is Location[4]
Bathroom = 5        ##Bathroom     is Location[5]
Window = 6          ##Window       is Location[6]
Closet = 7          ##Closet       is Location[7]
Porch = 8           ##Porch        is Location[8]
Ending = 9          ##Ending       is Location[9]

Location = ["You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...",
            "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces,\n and there are no counters or cabinents anywhere.", 
            "You walk into a dimly lit dinning room. The table is cracked in many places, and the chairs look like they haven't been\nused in years.", 
            "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls.\nYou see a family room to your left, a window in front of you, and a bathroom to your right.", 
            "You enter the family room. The only thing is in the room is a couch with a picture resting on it.\nUpon further inspection, the picture has been scratched out a replaced with " + pName + " written in blood.", 
            "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words\nwritten in the slime: Do you like to float " + pName + "?",
            "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it,\nand for a second you think you see something move...\nYou see a closet to your left, and a door out to the porch to your right.",
            "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",
            "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",
            "You hear shuffling behind you. You turn around to find a clown behind you. \"Hello " + pName + ", it's time to float.\" the clown says laughing maniacally.\nYou try to run away but it grabs you and drags you downstairs..."]

                        ##Visits List:
visitKitchen = 0        ##visitKitchen     is Visits[0]
visitDiningRoom = 1     ##visitDiningRoom  is Visits[1]
visitHallway = 2        ##visitHallway     is Visits[2]
visitFamilyRoom = 3     ##visitFamilyRoom  is Visits[3]
visitBathroom = 4       ##visitBathroom    is Visits[4]
visitWindow = 5         ##visitWindow      is Visits[5]
visitCloset = 6         ##visitCloset      is Visits[6]
visitPorch = 7          ##visitPorch       is Visits[7]
endVar = 8              ##endVar           is Visits[8]

Visits = [False, False, False, False, False, False, False, False, False]


            
##Shows introduction and starting location

def startProgram():
    global pScore, pLocation
        
    print("Hello", pName + "! Welcome to")
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
    pLocation = Location[0]     ##Foyer

def playGame():
    global Command, pLocation, Location, Visits, endVar

    while Visits[endVar] == False:   ##Boolean variable to be able to end the game when the player's score equals 45
        print("\n" + pLocation + "\n")
        print("=================================================\n")
        goTo()
    else:
        print("\n" + pLocation + "\n")
        EndGame()

def goTo():
    global Command, pScore, pLocation, pName, Visits, Location, Kitchen, pStart, DiningRoom
    global FamilyRoom, Hallway, Bathroom, Closet, Window, Porch, visitKitchen, visitDiningRoom
    global visitFamilyRoom, visitHallway, visitBathroom, visitCloset, visitWindow, visitPorch, endVar
    
    Command = input("Please input a command: ")
    Command = Command.lower()
    
    print()
    if Command == 'help' or Command == 'forward' or Command == 'back' or Command == 'right' or Command == 'left' or Command == 'points' or Command == 'map':
        if Command == 'help':
            print("List of commands:\nForward, Back, Right, Left, Help, Quit, Points, Map\n")
            print("=================================================\n")
            goTo()
            
        if Command == 'points':
            print("Your score is", pScore)
            print("=================================================\n")
            goTo()

        if Command == 'map':
            from Map import showMap
            goTo()
                
        if Command == 'forward':
            if pLocation == Location[pStart]:
                pLocation = Location[Hallway]
                if Visits[visitHallway] == False:
                    pScore += 5
                    Visits[visitHallway] = True
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[Hallway]:
                pLocation = Location[Window]
                if Visits[visitWindow] == False:
                    pScore += 5
                    Visits[visitWindow] = True
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            else:
                if pScore != 45:
                    print("Oops. There's a wall in the way. Try again.")
                    goTo()
                
        if Command == 'back':
            if pLocation == Location[Kitchen]:
                pLocation = Location[pStart]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[DiningRoom]:
                pLocation = Location[pStart]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[Hallway]:
                pLocation = Location[pStart]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[Window]:
                pLocation = Location[Hallway]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[FamilyRoom]:
                pLocation = Location[Hallway]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[Bathroom]:
                pLocation = Location[Hallway]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[Closet]:
                pLocation = Location[Window]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            elif pLocation == Location[Porch]:
                pLocation = Location[Window]
                if pScore == 45:
                    Visits[endVar] = True
                playGame()
            else:
                if pScore != 45:
                    print("Oops. There's a wall in the way. Try again.")
                    goTo()
                
        if Command == 'right':
            if pLocation == Location[0]:        ##Foyer
                pLocation = Location[2]         ##Moves player to Dining Room
                if Visits[1] == False:
                    pScore += 5
                    Visits[1] = True            ##If the player hasn't visited the Dining Room, adds 5 to player's score
                if pScore == 45:
                    Visits[8] = True            ##Sets endgame variable to true
                playGame()
            elif pLocation == Location[3]:      ##Hallway
                pLocation = Location[5]         ##Moves player to Bathroom
                if Visits[4] == False:
                    pScore += 5
                    Visits[4] = True            ##If player hasn't visited the Bathroom, adds 5 to player's score
                if pScore == 45:
                    Visits[8] = True            ##Sets endgame variable to true
                playGame()
            elif pLocation == Location[6]:      ##Window
                pLocation = Location[8]         ##Moves player to Porch
                if Visits[7] == False:
                    pScore += 5
                    Vists[7] = True             ##If the player hasn't visited the Porch, adds 5 to player's score
                if pScore == 45:
                    Visits[8] = True            ##Sets endgame variable to true
                playGame()
            else:
                if pScore != 45:
                    print("Oops. There's a wall in the way. Try again.")
                    goTo()
                
        if Command == 'left':
            if pLocation == Location[0]:        ##Foyer
                pLocation = Location[1]         ##Moves player to Kitchen
                if Visits[0] == False:
                    pScore += 5
                    Visits[0] = True            ##If the player hasn't visited the Kitchen, adds 5 to player's score
                if pScore == 45:
                    Visits[8] = True            ##Sets endgame variable to true
                playGame()
            elif pLocation == Location[3]:      ##Hallway
                pLocation = Location[4]         ##Moves player to Family Room
                if Visits[3] == False:
                    pScore += 5
                    Visits[3] = True            ##If the player hasn't visited the Family Room, adds 5 to player's score
                if pScore == 45:
                    Visits[8] = True            ##Sets endgame variable to true
                playGame()
            elif pLocation == Location[6]:      ##Hallway
                pLocation = Location[7]         ##Moves player to Closet
                if Visits[6] == False:
                    pScore += 5
                    Visits[6] = True            ##If player hasn't visited the Closet, adds 5 to player's score
                if pScore == 45:
                    Visits[8] = True            ##Sets endgame variable to true
                playGame()
            else:
                if pScore != 45:
                    print("Oops. There's a wall in the way. Try again.")
                    goTo()
    elif Command == 'quit':
        quit()
    else:
        print("Please input a valid command, or type 'help' to view a list of valid commands.")
        print("=================================================\n")
        goTo()
        

def EndGame():
    global Ending
    print(Location[Ending])
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")
    quit()


startProgram()
playGame()
