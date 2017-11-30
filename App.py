# CMPT Semester Project
# Author: David Siegel
# Version: 0.7

endCredits = "\nTHE END\n(c) 2017 David Siegel, idruless@gmail.com"

# Locations
# shortLoc = ["Foyer", "Kitchen", "Dining Room", "Hallway", "Family Room", "Bathroom", "Window", "Closet", "Porch", "Bedroom", "Hidden Room"]
# pStart      = 0
# Kitchen     = 1
# DiningRoom  = 2
# Hallway     = 3
# FamilyRoom  = 4
# Bathroom    = 5
# Window      = 6
# Closet      = 7
# Porch       = 8
# Bedroom     = 9
# HiddenRoom  = 10

# Location Matrix

#           Items List
#           Foyer   Kitchen   Dining Room   Hallway  Family Room   Bathroom   Window   Closet  Porch  Bedroom  Hidden Room
# ItemLoc =   [ None, "knife",   None,         "map",   None,         "key",     None,    None,   None,  None,    None        ]

# Boolean variables to keep track if the player has search a certain location
# hasSearched = [ False, False, False, False, False, False, False, False, False, False ]

# First "False" value is placeholder for pStart/Foyer. Other indexes are same as location values
# pStart/Foyer   Kitchen  DiningRoom  Hallway  FamilyRoom  Bathroom  Window  Closet  Porch  Bedroom  HiddenRoom  Ending
# Visits = [ False, False  , False     , False  , False     , False   , False , False , False, False  , False     , False ]


class Player:
    def __init__(self, name, score, location, moveCount, inventory):
        self.name = name
        self.score = score
        self.location = location
        self.moveCount = moveCount
        self.inventory = inventory

    def addScore(self):
        self.score += 5

    def addMove(self):
        self.moveCount += 1

    def getName(self):
        self.name = input("What is your name? ")

    def moveTo(self, currLoc, direction):
        newLoc = Location[currLoc.value][direction]
        if newLoc != None:
            self.location = newLoc
        else:
            print("Oops! You can't go there! Please try again.\n")
        getInput()


class Locale:
    def __init__(self, name, value, longDes, shortDes, wasVisited, wasSearched, items):
        self.name = name
        self.value = value
        self.longDes = longDes
        self.shortDes = shortDes
        self.wasVisited = wasVisited
        self.wasSearched = wasSearched
        self.items = items

    def showLongName(self):
        print(self.longDes)

    def showShortName(self):
        print(self.shortDes)

    def showItems(self):
        print(self.items)


# <editor-fold desc="pStart/Foyer">
pStart = Locale("pStart/Foyer",  # name
                0,
                "You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...", # longDes
                "Foyer",  # shortDes
                False,  # wasVisited
                False,  # wasSearched
                None  # items
                )
# </editor-fold>

# <editor-fold desc="Kitchen">
Kitchen = Locale("Kitchen",  # name
                 1,
                 "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces," +
                 "\n and there are no counters or cabinets anywhere.",  # longDes
                 "Kitchen",  # shortDes
                 False,  # wasVisited
                 False,  # wasSearched
                 "knife"  # items
                 )
# </editor-fold>

# <editor-fold desc="DiningRoom">
DiningRoom = Locale("Dining Room",
                    2,
                    "You walk into a dimly lit dinning room. The table is cracked in many places, " +
                    "and the chairs look like they haven't been\nused in years.",
                    "Dining Room",
                    False,
                    False,
                    None
                    )
# </editor-fold>

# <editor-fold desc="Hallway">
Hallway = Locale("Hallway",
                 3,
                 "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls." +
                 "\nYou see a family room to your left, a window in front of you, and a bathroom to your right.",
                 "Hallway",
                 False,
                 False,
                 "map"
                 )
# </editor-fold>

# <editor-fold desc="FamilyRoom">
FamilyRoom = Locale("Family Room",
                    4,
                    "You enter the family room. The only thing is in the room is a couch with a picture resting on it." +
                    "\nUpon further inspection, the picture has been scratched out a replaced with " + pName + " written in blood.",
                    "Family Room",
                    False,
                    False,
                    None
                    )
# </editor-fold>

# <editor-fold desc="Bathroom">
Bathroom = Locale("Bathroom",
                  5,
                  "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words" +
                  "\nwritten in the slime: Do you like to float " + pName + "?",
                  "Bathroom",
                  False,
                  False,
                  "key"
                  )
# </editor-fold>

# <editor-fold desc="Window">
Window = Locale("Window",
                6,
                "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it," +
                "\nand for a second you think you see something move...\nYou see a closet to your left, and a door out to the porch to your right.",
                "Window",
                False,
                False,
                None
                )
# </editor-fold>

# <editor-fold desc="Closet">
Closet = Locale("Closet",
                7,
                "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",
                "Closet",
                False,
                False,
                None
                )
# </editor-fold>

# <editor-fold desc="Porch">
Porch = Locale("Porch",
               8,
               "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",
               "Porch",
               False,
               False,
               None
               )
# </editor-fold>

# <editor-fold desc="Bedroom">
Bedroom = Locale("Bedroom",
                 9,
                 "You walk into an old bedroom. You see an old four-poster bed, and a small couch in the corner. Dust has settled over the entire room.",
                 "Bedroom",
                 False,
                 False,
                 None
                 )
# </editor-fold>

# <editor-fold desc="HiddenRoom">
HiddenRoom = Locale("Hidden Room",
                    10,
                    "",
                    "Hidden Room",
                    False,
                    False,
                    None
                    )
# </editor-fold>


Location = [  # North       South       East            West
    [Hallway,               None,       DiningRoom,     Kitchen     ],  # pStart/Foyer
    [None,                  None,       pStart,         None        ],  # Kitchen
    [None,                  None,       None,           pStart      ],  # Dining Room
    [Window,                pStart,     Bathroom,       FamilyRoom  ],  # Hallway
    [None,                  None,       Hallway,        Bedroom     ],  # Family Room
    [None,                  None,       None,           Hallway     ],  # Bathroom
    [None,                  Hallway,    Porch,          Closet      ],  # Window
    [None,                  None,       Window,         HiddenRoom  ],  # Closet
    [None,                  None,       None,           Window      ],  # Porch
    [None,                  None,       FamilyRoom,     None        ],  # Bedroom
    [None,                  None,       Closet,         None        ]   # Hidden Room
]

Player1 = Player("",
                 0,
                 pStart,
                 0,
                 []
                 )


# Description = [
#        ## pStart/Foyer
#        "You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...",
#
#        ## Kitchen
#        "You walk into the kitchen. Or what's left of it... The fridge has no doors, the stove is ripped to pieces," +
#        "\n and there are no counters or cabinents anywhere.",
#
#        ## Dining Room
#        "You walk into a dimly lit dinning room. The table is cracked in many places, " +
#        "and the chairs look like they haven't been\nused in years.",
#
#        ## Hallway
#        "You walk into a dark, narrow hallway. There are faceless pictures hanging on both walls." +
#        "\nYou see a family room to your left, a window in front of you, and a bathroom to your right.",
#
#        ## Family Room
#        "You enter the family room. The only thing is in the room is a couch with a picture resting on it." +
#        "\nUpon further inspection, the picture has been scratched out a replaced with " + pName + " written in blood.",
#
#        ## Bathroom
#        "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words" +
#        "\nwritten in the slime: Do you like to float " + pName + "?",
#
#        ## Window
#        "You walk up to the window. The wood is cracking and the paint on the border is peeling. You look out through it," +
#        "\nand for a second you think you see something move...\nYou see a closet to your left, and a door out to the porch to your right.",
#
#        ## Closet
#        "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",
#
#        ## Porch
#        "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",
#
#        ## Bedroom
#        "You walk into an old bedroom. You see an old four-poster bed, and a small couch in the corner. Dust has settled over the entire room.",
#
#        ## Hidden Room
#        ""]


##Shows introduction and starting location
def startProgram():
    Player.getName(Player1)
    print("Hello", Player1.name + "! Welcome to")
    print(" _____ _     _____           _     ___")
    print("|_   _| |   |  __ \         | |   |__ \ ")
    print("  | | | |_  | |__) |_ _ _ __| |_     ) |")
    print("  | | | __| |  ___/ _` | '__| __|   / / ")
    print(" _| |_| |_  | |  | (_| | |  | |_   / /_ ")
    print("|_____|\__| |_|   \__,_|_|   \__| |____|")
    print("\nBy: David Siegel")
    print(
        "You are in front of an abandoned house, late on Halloween night.You went there looking for your friends who ran off ahead of you.\n" +
        "You move to the front door and go inside. You walk inside and the door suddenly slams closed behind you...\n")
    input("Press a key to continue")

    Player.addScore(Player1)


# Shows map
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


# Initiates game sequence
def playGame():
    if Player.location.wasVisited:
        print("\nYou are at the " + Locale.shortDes + "\n")
        print("=================================================\n")
    else:
        print("\n" + Player.location.longDes + "\n")
        print("=================================================\n")
    Player.location.wasVisited = True
    getInput()


def moveTo(currLoc, direction):
    newLoc = Location[currLoc][direction]
    if newLoc != None:
        return newLoc
    else:
        print("Oops! You can't go there! Please try again.\n")
        getInput()


# Searches the player's current location for any items
def locSearch(currLoc):
    noItems = "Sorry, there are no items in this location."
    if currLoc.wasSearched == False:
        currLoc.wasSearched = True
    if currLoc.items != None:
        return currLoc.items
    else:
        return noItems


# Moves player around game world based on user input
def getInput():
    global pName, pLocation

    North = 0
    South = 1
    East = 2
    West = 3

    Command = input("Please input a command: ")
    Command = Command.lower()

    print()
    if Command == 'north' or Command == 'south' or Command == 'east' or Command == 'west':
        if Command == 'north':
            pLocation = moveTo(Player.location.name, North)
            if Player.location.wasVisited == False:
                Player.addScore()
                Player.location.wasVisited = True
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
        if Player.location.hasSearched:
            Player.inventory.append(Player.location.items)
            Player.location.remove(Player.location.items)
        else:
            print("You don't know if anything is there.")
        print("\n=================================================\n")
        getInput()

    elif Command == 'map':
        if 'map' in Player.inventory:
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
        print(Player.location.longDes)
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
    print(
        "You insert the key into the door, unlock it, and enter the hidden room. Just as you are closing the door after you,\n" +
        "you heard loud, fast footsteps coming towards you. Luckily, you shut the door in time and are now safe.")
    print(endCredits)
    quit()


## Shows game lose ending
def endLose():
    print(
        "You hear shuffling behind you. You turn around to find a clown behind you. \"Hello " + pName + ", it's time to float.\" " +
        "the clown says laughing maniacally.\nYou try to run away but it grabs you and drags you into the hidden room...")
    print(endCredits)
    quit()


startProgram()
playGame()
