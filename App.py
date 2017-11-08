##CMPT Semester Project
##Author: David Siegel
##Version: 0.7

pLocation = 0
pName = input("What is your name? ")
pScore = 0


## Locations
shortLoc = ["Foyer", "Kitchen", "Dining Room", "Hallway", "Family Room", "Bathroom", "Window", "Closet", "Porch", "Bedroom", "Hidden Room"]

pStart      = 0
Kitchen     = 1
DiningRoom  = 2
Hallway     = 3
FamilyRoom  = 4
Bathroom    = 5
Window      = 6
Closet      = 7
Porch       = 8
Bedroom     = 9
HiddenRoom  = 10
Ending      = 11


## Location Matrix
Location =   [ ## North        South             East              West
        [ Hallway,        None   ,             DiningRoom,       Kitchen    ] ## pStart/Foyer
    ,   [ None   ,        None   ,             pStart    ,       None       ] ## Kitchen
    ,   [ None   ,        None   ,             None      ,       pStart     ] ## Dining Room
    ,   [ Window ,        pStart ,             Bathroom  ,       FamilyRoom ] ## Hallway
    ,   [ None   ,        None   ,             Hallway   ,       Bedroom    ] ## Family Room
    ,   [ None   ,        None   ,             None      ,       Hallway    ] ## Bathroom
    ,   [ None   ,        Hallway,             Porch     ,       Closet     ] ## Window
    ,   [ None   ,        None   ,             Window    ,       HiddenRoom ] ## Closet
    ,   [ None   ,        None   ,             None      ,       Window     ] ## Porch
    ,   [ None   ,        None   ,             FamilyRoom,       None       ] ## Bedroom
    ,   [ None   ,        None   ,             Closet    ,       None       ] ## Hidden Room
    ]


##           Items List
##           Foyer   Kitchen   Dining Room   Hallway  Family Room   Bathroom   Window   Closet  Porch  Bedroom  Hidden Room
ItemLoc =   [ None, "knife",   None,         "map",   None,         "key",     None,    None,   None,  None,    None        ]


## First "True" value is placeholder for pStart/Foyer. Other indexes are same as location values
Visits = [True, False, False, False, False, False, False, False, False, False, False, False]


## Inventory List
Inventory = []


Description = [
        ## pStart/Foyer
        "You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...",

        ## Kitchen
        "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces," +
        "\n and there are no counters or cabinents anywhere.",

        ## Dining Room
        "You walk into a dimly lit dinning room. The table is cracked in many places, " +
        "and the chairs look like they haven't been\nused in years.",

        ## Hallway
        "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls." +
        "\nYou see a family room to your left, a window in front of you, and a bathroom to your right.",

        ## Family Room
        "You enter the family room. The only thing is in the room is a couch with a picture resting on it." +
        "\nUpon further inspection, the picture has been scratched out a replaced with " + pName + " written in blood.",

        ## Bathroom
        "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words" +
        "\nwritten in the slime: Do you like to float " + pName + "?",

        ## Window
        "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it," +
        "\nand for a second you think you see something move...\nYou see a closet to your left, and a door out to the porch to your right.",

        ## Closet
        "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",

        ## Porch
        "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",

        ## Bedroom
        "You walk into an old bedroom. You see an old four-poster bed, and a small couch in the corner. Dust has settled over the entire room.",

        ## Hidden Room
        "",

        ## Ending
        "You hear shuffling behind you. You turn around to find a clown behind you. \"Hello " + pName + ", it's time to float.\" " +
        "the clown says laughing maniacally.\nYou try to run away but it grabs you and drags you downstairs..."]


##Shows introduction and starting location
def startProgram():
    global pScore, pLocation, pStart, Description

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
    pLocation = pStart


## Initiates game sequence
def playGame():
    global shortLoc, pStart
    print("\nYou are at the " + shortLoc[pLocation] + "\n")
    print("=================================================\n")
    goTo()


## Moves player based on current location and user input
def movePlayer(currLoc, direction):
    newLoc = Location[currLoc][direction]
    if newLoc != None:
        return newLoc
    else:
        print("Oops! You can't go there! Please try again.\n")
        goTo()


## Moves player around game world based on user input
def goTo():
    global pScore, pLocation, pName, Visits, Description, Kitchen, pStart, DiningRoom
    global FamilyRoom, Hallway, Bathroom, Closet, Window, Porch, Location

    North = 0
    South = 1
    East  = 2
    West  = 3

    Command = input("Please input a command: ")
    Command = Command.lower()

    print()
    if Command == 'north' or Command == 'south' or Command == 'east' or Command == 'west':
        if Command == 'north':
            pLocation = movePlayer(pLocation, North)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            playGame()

        elif Command == 'south':
            pLocation = movePlayer(pLocation, South)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            playGame()

        if Command == 'east':
            pLocation = movePlayer(pLocation, East)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            playGame()

        if Command == 'west':
            pLocation = movePlayer(pLocation, West)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            playGame()

    elif Command == 'map':
        from Map import showMap
        input("\nPress <Enter> to continue")
        print("\n=================================================\n")
        goTo()
                    
    elif Command == 'help':
        print("List of commands:\nNorth, South, East, West, Help, Quit, Points, Map, Look, Search, and Take\n")
        print("=================================================\n")
        goTo()
        
    elif Command == 'look':
        print(Description[pLocation])
        print("=================================================\n")
        goTo()

        
    elif Command == 'points':
        print("Your score is", pScore)
        print("=================================================\n")
        goTo()

    elif Command == 'quit':
        quit()
        
    else:
        print("Please input a valid command, or type 'help' to view a list of valid commands.")
        print("=================================================\n")
        goTo()


## Displays game ending
def EndGame():
    global Description, Ending
    print(Description[Ending])
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")
    quit()


startProgram()
playGame()
