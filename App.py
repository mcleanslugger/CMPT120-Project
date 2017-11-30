# CMPT Semester Project
# Author: David Siegel
# Version: 0.7

endCredits = "\nTHE END\n(c) 2017 David Siegel, idruless@gmail.com"


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
        playGame()

    def locSearch(self, currLoc):
        noItems = "Sorry, there are no items in this location."
        if currLoc.wasSearched == False:
            currLoc.wasSearched = True
        if currLoc.items != None:
            return currLoc.items
        else:
            return noItems


class Locale(object):
    def __init__(self, name, value, longDes, shortDes, wasVisited, wasSearched, items):
        self.name = name
        self.value = value
        self.longDes = longDes
        self.shortDes = shortDes
        self.wasVisited = wasVisited
        self.wasSearched = wasSearched
        self.items = items


# <editor-fold desc="Player1">
Player1 = Player("",
                 0,
                 None,
                 0,
                 []
                 )
# </editor-fold>


# <editor-fold desc="pStart/Foyer">
pStart = Locale("pStart/Foyer",  # name
                0,
                "You enter the foyer. You see a kitchen to your left, a dinning room to your right, and a long hallway in front of you...", # longDes
                "Foyer",  # shortDes
                False,  # wasVisited
                False,  # wasSearched
                [None]  # items
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
                 ['knife']  # items
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
                    [None]
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
                 ['map']
                 )
# </editor-fold>

# <editor-fold desc="FamilyRoom">
FamilyRoom = Locale("Family Room",
                    4,
                    "You enter the family room. The only thing is in the room is a couch with a picture resting on it." +
                    "\nUpon further inspection, the picture has been scratched out a replaced with " + Player1.name + " written in blood.",
                    "Family Room",
                    False,
                    False,
                    [None]
                    )
# </editor-fold>

# <editor-fold desc="Bathroom">
Bathroom = Locale("Bathroom",
                  5,
                  "You enter the bathroom. It is covered in grime and slime, but on the miror above the sink there are a few words" +
                  "\nwritten in the slime: Do you like to float " + Player1.name + "?",
                  "Bathroom",
                  False,
                  False,
                  ['key']
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
                [None]
                )
# </editor-fold>

# <editor-fold desc="Closet">
Closet = Locale("Closet",
                7,
                "You open the closet door, and it is filled with red balloons... You instantly get uneasy and start panicking.",
                "Closet",
                False,
                False,
                [None]
                )
# </editor-fold>

# <editor-fold desc="Porch">
Porch = Locale("Porch",
               8,
               "You walk out onto the porch, and you see that the wood railing is broken. It's so dark outside you can't see anything past the porch...",
               "Porch",
               False,
               False,
               [None]
               )
# </editor-fold>

# <editor-fold desc="Bedroom">
Bedroom = Locale("Bedroom",
                 9,
                 "You walk into an old bedroom. You see an old four-poster bed, and a small couch in the corner. Dust has settled over the entire room.",
                 "Bedroom",
                 False,
                 False,
                 [None]
                 )
# </editor-fold>

# <editor-fold desc="HiddenRoom">
HiddenRoom = Locale("Hidden Room",
                    10,
                    "",
                    "Hidden Room",
                    False,
                    False,
                    [None]
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
    if Player1.location.wasVisited:
        print("\nYou are at the " + Player1.location.shortDes + "\n")
        print("=================================================\n")
    else:
        print("\n" + Player1.location.longDes + "\n")
        print("=================================================\n")
    getInput()


# Moves player around game world based on user input
def getInput():
    North = 0
    South = 1
    East = 2
    West = 3

    Command = input("Please input a command: ")
    Command = Command.lower()

    print()
    if Command == 'north' or Command == 'south' or Command == 'east' or Command == 'west':
        if Command == 'north':
            Player.moveTo(Player1, Player1.location, North)
            if Player1.location.wasVisited == False:
                Player1.location.wasVisited = True
                Player.addScore(Player1)
            playGame()

        if Command == 'south':
            Player.moveTo(Player1, Player1.location, South)
            if Player1.location.wasVisited == False:
                Player1.location.wasVisited = True
                Player.addScore(Player1)
            playGame()

        if Command == 'east':
            Player.moveTo(Player1, Player1.location, East)
            if Player1.location.wasVisited == False:
                Player1.location.wasVisited = True
                Player.addScore(Player1)
            playGame()

        if Command == 'west':
            Player.moveTo(Player1, Player1.location, West)
            if Player1.location.wasVisited == False:
                Player1.location.wasVisited = True
                Player.addScore(Player1)
            if Player1.location.value == 10:
                if 'key' in Player1.inventory:
                    endWin()
                else:
                    endLose()
            playGame()

    if Command == 'search':
        print(Player.locSearch(Player1, Player1.location))
        print("\n=================================================\n")
        getInput()

    if Command == 'take':
        cmd = input("Enter item to take: ")
        cmd = cmd.lower()
        print()

        if cmd in Player1.location.items:
            if Player1.location.wasSearched:
                Player1.inventory.append(cmd)
                Player1.location.items.remove(cmd)
                Player1.location.items = None
                print("Your inventory is now: " + str(Player1.inventory))
            else:
                print("You don't know that is there.")
        else:
            print("That item is not here.")
        print("\n=================================================\n")
        getInput()

    elif Command == 'map':
        if 'map' in Player1.inventory:
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
        print(Player.showLongName(Player1))
        print("\n=================================================\n")
        getInput()

    elif Command == 'points':
        print("Your score is", Player1.score)
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
        "You hear shuffling behind you. You turn around to find a clown behind you. \"Hello " + Player1.name + ", it's time to float.\" " +
        "the clown says laughing maniacally.\nYou try to run away but it grabs you and drags you into the hidden room...")
    print(endCredits)
    quit()


startProgram()
Player1.location = pStart
playGame()
