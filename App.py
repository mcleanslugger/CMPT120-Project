##CMPT Semester Project
##Author: David Siegel
##Version: 0.7

endCredits = "\nTHE END\n(c) 2017 David Siegel, idruless@gmail.com"

## Locations
## shortLoc = ["Foyer", "Kitchen", "Dining Room", "Hallway", "Family Room", "Bathroom", "Window", "Closet", "Porch", "Bedroom", "Hidden Room"]
##pStart      = 0
##Kitchen     = 1
##DiningRoom  = 2
##Hallway     = 3
##FamilyRoom  = 4
##Bathroom    = 5
##Window      = 6
##Closet      = 7
##Porch       = 8
##Bedroom     = 9
##HiddenRoom  = 10

## Location Matrix
Location = [##North       South                East              West
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
##ItemLoc =   [ None, "knife",   None,         "map",   None,         "key",     None,    None,   None,  None,    None        ]

## Boolean variables to keep track if the player has search a certain location
##hasSearched = [ False, False, False, False, False, False, False, False, False, False ]

## First "False" value is placeholder for pStart/Foyer. Other indexes are same as location values
## pStart/Foyer   Kitchen  DiningRoom  Hallway  FamilyRoom  Bathroom  Window  Closet  Porch  Bedroom  HiddenRoom  Ending
##Visits = [ False, False  , False     , False  , False     , False   , False , False , False, False  , False     , False ]


class Player:
    name = ""
    score = 0
    location = 0
    moveCount = 0
    inventory = []

    def __init__(self, name, score, location, moveCount, inventory):
        Player.name = name
        Player.score = score
        Player.location = location
        Player.moveCount = moveCount
        Player.inventory = inventory

    def addScore(self):
        self.score += 5

    def addMove(self):
        self.moveCount +=1

    def getName(self):
        self.name = input("What is your name? ")

    def moveTo(self, direction):
        newLoc = Location[Player.location][direction]
        if newLoc != None:
            Player.location = newLoc
        else:
            print("Oops! You can't go there! Please try again.\n")
            getInput()


class Locale:
    name = ""
    value = 0
    longDes = ""
    shortDes = ""
    wasVisited = False
    wasSearched = True
    items = ""

    def __init__(self, name, value, longDes, shortDes, wasVisited, wasSearched, items):
        Locale.name = name
        Locale.value = value
        Locale.longDes = longDes
        Locale.shortDes = shortDes
        Locale.wasVisited = wasVisited
        Locale.wasSearched = wasSearched
        Locale.items = items

    def showLongName(self):
        print(self.longDes)

    def showShortName(self):
        print(self.shortDes)

    def showItems(self):
        print(self.items)

## Locations
pStart =    Locale( "Foyer",        ## name
                    0,              ## value used for indexing matrices
                    "You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...", ## longDes
                    "Foyer",        ## shortDes
                    False,          ## wasVisited
                    False,          ## wasSearched
                    None            ## items
                    )

Kitchen =   Locale( "Kitchen",      ## name
                    1,              ## value used for indexing matrices
                    "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces," +
                    "\n and there are no counters or cabinents anywhere.", ## longDes
                    "Kitchen",      ## shortDes
                    False,          ## wasVisited
                    False,          ## wasSearched
                    "knife"         ## items
                    )

DiningRoom= Locale( "Dining Room",
                    2,
                    "You walk into a dimly lit dinning room. The table is cracked in many places, " +
                    "and the chairs look like they haven't been\nused in years.",
                    "Dining Room",
                    False,
                    False,
                    None
                    )

Hallway =   Locale( "Hallway",
                    3,
                    "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls." +
                    "\nYou see a family room to your left, a window in front of you, and a bathroom to your right.",
                    "Hallway",
                    False,
                    False,
                    "map"
                    )

FamilyRoom= Locale( "Family Room",
                    4,
                    "You enter the family room. The only thing is in the room is a couch with a picture resting on it." +
                    "\nUpon further inspection, the picture has been scratched out a replaced with " + Player.name + " written in blood.",
                    "Family Room",
                    False,
                    False,
                    None
                    )

Bathroom =  Locale( "Bathroom",
                    5,
                    "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words" +
                    "\nwritten in the slime: Do you like to float " + Player.name + "?",
                    "Bathroom",
                    False,
                    False,
                    "key"
                    )

Window =    Locale( "Window",
                    6,
                    "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it," +
                    "\nand for a second you think you see something move...\nYou see a closet to your left, and a door out to the porch to your right.",
                    "Window",
                    False,
                    False,
                    None
                    )

Closet =    Locale( "Closet",
                    7,
                    "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",
                    "Closet",
                    False,
                    False,
                    None
                    )

Porch =     Locale( "Porch",
                    8,
                    "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",
                    "Porch",
                    False,
                    False,
                    None
                    )

Bedroom =   Locale( "Bedroom",
                    9,
                    "You walk into an old bedroom. You see an old four-poster bed, and a small couch in the corner. Dust has settled over the entire room.",
                    "Bedroom",
                    False,
                    False,
                    None
                    )

HiddenRoom= Locale( "Hidden Room",
                    10,
                    "",
                    "Hidden Room",
                    False,
                    False,
                    None
                    )


##Description = [
##        ## pStart/Foyer
##        "You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...",
##
##        ## Kitchen
##        "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces," +
##        "\n and there are no counters or cabinents anywhere.",
##
##        ## Dining Room
##        "You walk into a dimly lit dinning room. The table is cracked in many places, " +
##        "and the chairs look like they haven't been\nused in years.",
##
##        ## Hallway
##        "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls." +
##        "\nYou see a family room to your left, a window in front of you, and a bathroom to your right.",
##
##        ## Family Room
##        "You enter the family room. The only thing is in the room is a couch with a picture resting on it." +
##        "\nUpon further inspection, the picture has been scratched out a replaced with " + Player.name + " written in blood.",
##
##        ## Bathroom
##        "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words" +
##        "\nwritten in the slime: Do you like to float " + Player.name + "?",
##
##        ## Window
##        "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it," +
##        "\nand for a second you think you see something move...\nYou see a closet to your left, and a door out to the porch to your right.",
##
##        ## Closet
##        "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",
##
##        ## Porch
##        "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",
##
##        ## Bedroom
##        "You walk into an old bedroom. You see an old four-poster bed, and a small couch in the corner. Dust has settled over the entire room.",
##
##        ## Hidden Room
##        ""]


##Shows introduction and starting location
def startProgram():
    Player.getName(Player)
    print("Hello", Player.name + "! Welcome to")
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

    Player.addScore(Player)
    Player.changeLocation(Player, pStart)

## Shows map
def showMap():
    print()
    print("     ==============================================================     ")
    print("                                                                        ")
    print("       Hidden Room --- Closet --------- Window --------- Porch          ")
    print("                                          ||                            ")
    print("                                          ||                            ")
    print("       Bedroom ----- Family Room ------ Hallway ------- Bathroom        ")
    print("                                          ||                            ")
    print("                                          ||                            ")
    print("                       Kitchen -------- Foyer ------- Dining Room       ")
    print("                                                                        ")
    print("     ==============================================================     ")

## Initiates game sequence
def playGame():
    global Visits, Description
    if Player.location.wasVisited == True:
        print("\nYou are at the " + Locale.shortDes + "\n")
        print("=================================================\n")
    else:
        print("\n" + Player.location.longDes + "\n")
        print("=================================================\n")
    Player.location.wasVisited = True
    getInput()


## Moves player based on current location and user input
def moveTo(currLoc, direction):
    newLoc = Location[currLoc][direction]
    if newLoc != None:
        return newLoc
    else:
        print("Oops! You can't go there! Please try again.\n")
        getInput()


## Searches the player's current location for any items
def locSearch(currLoc):
    noItems = "Sorry, there are no items in this location."
    if currLoc.wasSearched == False:
        currLoc.wasSearched = True
    if currLoc.items != None:
        return currLoc.items
    else:
        return noItems


## Moves player around game world based on user input
def getInput():
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
            pLocation = moveTo(pLocation, North)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            playGame()

        elif Command == 'south':
            pLocation = moveTo(pLocation, South)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            playGame()

        if Command == 'east':
            pLocation = moveTo(pLocation, East)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            playGame()

        if Command == 'west':
            pLocation = moveTo(pLocation, West)
            if Visits[pLocation] == False:
                pScore += 5
                Visits[pLocation] = True
            if pLocation == HiddenRoom:
                if 'key' in Inventory:
                    endWin()
                else:
                    endLose()
            else:
                playGame()

    elif Command == 'search':
        print(locSearch(Player.location))
        print("\n=================================================\n")
        getInput()

    elif Command == 'take':
        if hasSearched[pLocation] == True:
            Inventory.append(locSearch(pLocation))
            ItemLoc.remove(locSearch(pLocation))
        else:
            print("You don't know if anything is there.")
        print("\n=================================================\n")
        getInput()

    elif Command == 'map':
        if 'map' in Inventory:
            showMap()
            input("\nPress <Enter> to continue")
        else:
            print("You have no map to look at.")
        print("\n=================================================\n")
        getInput()

    elif Command == 'help':
        print("List of commands:\nNorth, South, East, West, Help, Quit, Points, Map, Look, Search, and Take\n")
        print("\n=================================================\n")
        getInput()

    elif Command == 'look':
        print(Description[pLocation])
        print("\n=================================================\n")
        getInput()


    elif Command == 'points':
        print("Your score is", pScore)
        print("\n=================================================\n")
        getInput()

    elif Command == 'quit':
        print(endCredits)
        quit()

    else:
        print("Please input a valid command, or type 'help' to view a list of valid commands.")
        print("\n=================================================\n")
        getInput()


## Shows game win ending
def endWin():
    print("You insert the key into the door, unlock it, and enter the hidden room. Just as you are closing the door after you,\n" +
          "you heard loud, fast footsteps coming towards you. Luckily, you shut the door in time and are now safe.")
    print(endCredits)
    quit()


## Shows game lose ending
def endLose():
    print("You hear shuffling behind you. You turn around to find a clown behind you. \"Hello " + pName + ", it's time to float.\" " +
          "the clown says laughing maniacally.\nYou try to run away but it grabs you and drags you into the hidden room...")
    print(endCredits)
    quit()


startProgram()
playGame()
