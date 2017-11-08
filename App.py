##CMPT Semester Project
##Author: David Siegel
##Version: 0.7

Command = ""
pLocation = 0
pName = input("What is your name? ")
pScore = 0
moves = 0


## Locations
shortLoc = ["pStart", "Kitchen", "Dining Room", "Hallway", "Family Room", "Bathroom", "Window", "Closet", "Porch"]
pStart = 0          ##pStart       is Description[0]
Kitchen = 1         ##Kitchen      is Description[1]
DiningRoom = 2      ##DiningRoom   is Description[2]
Hallway = 3         ##Hallway      is Description[3]
FamilyRoom = 4      ##FamilyRoom   is Description[4]
Bathroom = 5        ##Bathroom     is Description[5]
Window = 6          ##Window       is Description[6]
Closet = 7          ##Closet       is Description[7]
Porch = 8           ##Porch        is Description[8]
Ending = 9          ##Ending       is Description[9]


## Location Matrix
Location =   [ ## North        South             East              West
        [ Hallway,        None   ,             DiningRoom,       Kitchen    ] ## Starting location is pStart/Foyer
    ,   [ None   ,        None   ,             pStart    ,       None       ] ## Starting location is Kitchen
    ,   [ None   ,        None   ,             None      ,       pStart     ] ## Starting location is Dining Room
    ,   [ Window ,        pStart ,             Bathroom  ,       FamilyRoom ] ## Starting location is Hallway
    ,   [ None   ,        None   ,             Hallway   ,       None       ] ## Starting location is Family Room
    ,   [ None   ,        None   ,             None      ,       Hallway    ] ## Starting location is Bathroom
    ,   [ None   ,        Hallway,             Porch     ,       Closet     ] ## Starting location is Window
    ,   [ None   ,        None   ,             Window    ,       None       ] ## Starting location is Closet
    ,   [ None   ,        None   ,             None      ,       Window     ] ## Starting location is Porch
    ]


## First "False" value is placeholder for pStart/Foyer. Other indexes are same as location values
Visits = [False, False, False, False, False, False, False, False, False, False]


## Inventory List
Inventory = []


Description = ["You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...",

            "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces," +
            "\n and there are no counters or cabinents anywhere.",

            "You walk into a dimly lit dinning room. The table is cracked in many places, " +
            "and the chairs look like they haven't been\nused in years.",

            "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls." +
            "\nYou see a family room to your left, a window in front of you, and a bathroom to your right.",

            "You enter the family room. The only thing is in the room is a couch with a picture resting on it." +
            "\nUpon further inspection, the picture has been scratched out a replaced with " + pName + " written in blood.",

            "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words" +
            "\nwritten in the slime: Do you like to float " + pName + "?",

            "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it," +
            "\nand for a second you think you see something move...\nYou see a closet to your left, and a door out to the porch to your right.",

            "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",

            "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",

            "You hear shuffling behind you. You turn around to find a clown behind you. \"Hello " + pName + ", it's time to float.\" " +
            "the clown says laughing maniacally.\nYou try to run away but it grabs you and drags you downstairs..."]



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
    pScore += 5
    pLocation = Description[pStart]

## Initiates game sequence

def playGame():
    global Command, pLocation, Description, Visits, Ending

    while Visits[Ending] == False:      ##Boolean variable to be able to end the game when the player's score equals 45
            print("\nYou are at the " + shortLoc[pStart] + "\n")
            print("=================================================\n")
            goTo()

## Moves player around game world based on user input

def goTo():
    global Command, pScore, pLocation, pName, Visits, Description, Kitchen, pStart, DiningRoom
    global FamilyRoom, Hallway, Bathroom, Closet, Window, Porch

    Command = input("Please input a command: ")
    Command = Command.split().lower()

    print()
    if Command == 'help' or Command == 'north' or Command == 'south' or Command == 'east' or Command == 'west' or Command == 'points' or Command == 'map':
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
            playGame()

        if Command == 'north':
            if pLocation == Description[pStart]:
                pLocation = Description[Hallway]
                if Visits[Hallway] == False:
                    pScore += 5
                    Visits[Hallway] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Hallway]:
                pLocation = Description[Window]
                if Visits[Window] == False:
                    pScore += 5
                    Visits[Window] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            else:
                if pScore != 45:
                    print("Oops. There's a wall in the way. Try again.")
                    goTo()

        if Command == 'south':
            if pLocation == Description[Hallway]:
                pLocation = Description[pStart]
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Window]:
                pLocation = Description[Hallway]
                if Visits[Hallway] == False:
                    pScore += 5
                    Visits[Hallway] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            else:
                if pScore != 45:
                    print("Oops. There's a wall in the way. Try again.")
                    goTo()

        if Command == 'east':
            if pLocation == Description[pStart]:
                pLocation = Description[DiningRoom]
                if Visits[DiningRoom] == False:
                    pScore += 5
                    Visits[DiningRoom] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Hallway]:
                pLocation = Description[Bathroom]
                if Visits[Bathroom] == False:
                    pScore += 5
                    Visits[Bathroom] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Window]:
                pLocation = Description[Porch]
                if Visits[Porch] == False:
                    pScore += 5
                    Visits[Porch] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Kitchen]:
                pLocation = Description[pStart]
                if Visits[Kitchen] == False:
                    pScore += 5
                    Visits[Kitchen] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[FamilyRoom]:
                pLocation = Description[Hallway]
                if Visits[Hallway] == False:
                    pScore += 5
                    Visits[Hallway] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Closet]:
                pLocation = Description[Window]
                if Visits[Window] == False:
                    pScore += 5
                    Visits[Window] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            else:
                if pScore != 45:
                    print("Oops. There's a wall in the way. Try again.")
                    goTo()

        if Command == 'west':
            if pLocation == Description[pStart]:
                pLocation = Description[Kitchen]
                if Visits[Kitchen] == False:
                    pScore += 5
                    Visits[Kitchen] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Hallway]:
                pLocation = Description[FamilyRoom]
                if Visits[FamilyRoom] == False:
                    pScore += 5
                    Visits[FamilyRoom] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Window]:
                pLocation = Description[Closet]
                if Visits[Closet] == False:
                    pScore += 5
                    Visits[Closet] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[DiningRoom]:
                pLocation = Description[pStart]
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Bathroom]:
                pLocation = Description[Hallway]
                if Visits[Hallway] == False:
                    pScore += 5
                    Visits[Hallway] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
                playGame()
            elif pLocation == Description[Porch]:
                pLocation = Description[Window]
                if Visits[Window] == False:
                    pScore += 5
                    Visits[Window] = True
                if pScore == 45:
                    Visits[Ending] = True
                moves += 1
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

## Displays game ending

def EndGame():
    global Ending, moves
    if moves != 25:
        print(Description[Ending])
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")
    quit()


startProgram()
playGame()
