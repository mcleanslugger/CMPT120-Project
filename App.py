# CMPT Semester Project
# Author: David Siegel
# Version: 0.9

endCredits = "\nTHE END\n(c) 2017 David Siegel, idruless@gmail.com"

doorUnlocked = False


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
        if newLoc is not None:
            self.location = newLoc
        else:
            print("Oops! You can't go there! Please try again.\n")

    def locSearch(self, currLoc):
        noItems = "Sorry, there are no items in this location."
        if not currLoc.wasSearched:
            currLoc.wasSearched = True
        try:
            if None in currLoc.items:
                return noItems
            else:
                return currLoc.items
        except TypeError:
            return noItems

    def dropItem(self, item):
        try:
            Player1.location.items.append(str(item))
        except AttributeError:
            Player1.location.items = [str(item)]
        Player1.inventory.remove(item)

    def showInventory(self):
        return self.inventory


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
                "You enter the foyer. You see a kitchen to your left, a dinning room to your right,\n" +
                "and a long hallway in front of you...",  # longDes
                "Foyer",  # shortDes
                False,  # wasVisited
                False,  # wasSearched
                [None]  # items
                )
# </editor-fold>

# <editor-fold desc="Kitchen">
Kitchen = Locale("Kitchen",  # name
                 1,
                 "You walk into the kitchen. Or what's left of it..." +
                 "The fridge has no doors, the stove is ripped to pieces," +
                 "\n and there are no counters or cabinets anywhere." +
                 "You notice something by the fridge on the west side of the room...",  # longDes
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
                    "You enter the family room. The only thing is in the room is a couch with a picture" +
                    " resting on it.\nUpon further inspection, the picture has been scratched out " +
                    "and replaced with " + Player1.name + " written in blood.",
                    "Family Room",
                    False,
                    False,
                    ['key mold']
                    )
# </editor-fold>

# <editor-fold desc="Bathroom">
Bathroom = Locale("Bathroom",
                  5,
                  "You enter the bathroom. It is covered in grime and slime, but on " +
                  "the mirror above the sink there are a few words\nwritten in the slime: " +
                  "Do you like to float " + Player1.name + "?",
                  "Bathroom",
                  False,
                  False,
                  ['key putty']
                  )
# </editor-fold>

# <editor-fold desc="Window">
Window = Locale("Window",
                6,
                "You walk up to the window. The wood is cracking and the paint on the border is peeling. " +
                "You look out through it,\nand for a second you think you see something move..." +
                "\nYou see a closet to your left, and a door out to the porch to your right.",
                "Window",
                False,
                False,
                [None]
                )
# </editor-fold>

# <editor-fold desc="Closet">
Closet = Locale("Closet",
                7,
                "You open the closet door, and it is filled with red balloons... " +
                "You instantly get uneasy and start panicking.",
                "Closet",
                False,
                False,
                ['balloon']
                )
# </editor-fold>

# <editor-fold desc="Porch">
Porch = Locale("Porch",
               8,
               "You walk out onto the porch, and you see that the wood railing is broken. " +
               "It's so dark outside you can't see anything past the porch...",
               "Porch",
               False,
               False,
               ['flashlight']
               )
# </editor-fold>

# <editor-fold desc="Bedroom">
Bedroom = Locale("Bedroom",
                 9,
                 "You walk into an old bedroom. You see an old four-poster bed, " +
                 "and a small couch in the corner. Dust has settled over the entire room.",
                 "Bedroom",
                 False,
                 False,
                 [None]
                 )
# </editor-fold>

# <editor-fold desc="HiddenRoom">
HiddenRoom = Locale("Hidden Room",
                    10,
                    "You enter the hidden room behind the closet. " +
                    "There are no windows or any light coming into the room...",
                    "Hidden Room",
                    False,
                    False,
                    ['radio']
                    )
# </editor-fold>

# <editor-fold desc="SecretRoom">
SecretRoom = Locale("Secret Room",
                    11,
                    "You slip past the fridge and into the secret room. As you enter, " +
                    "you slide the fridge back to cover the entrance.",
                    "Secret Room",
                    False,
                    False,
                    [None]
                    )
# </editor-fold>


Location = [  # North       South       East            West
    [Hallway,               None,       DiningRoom,     Kitchen     ],  # pStart/Foyer
    [None,                  None,       pStart,         SecretRoom  ],  # Kitchen
    [None,                  None,       None,           pStart      ],  # Dining Room
    [Window,                pStart,     Bathroom,       FamilyRoom  ],  # Hallway
    [None,                  None,       Hallway,        Bedroom     ],  # Family Room
    [None,                  None,       None,           Hallway     ],  # Bathroom
    [None,                  Hallway,    Porch,          Closet      ],  # Window
    [None,                  None,       Window,         HiddenRoom  ],  # Closet
    [None,                  None,       None,           Window      ],  # Porch
    [None,                  None,       FamilyRoom,     None        ],  # Bedroom
    [None,                  None,       Closet,         None        ],  # Hidden Room
    [None,                  None,       Kitchen,        None        ]   # Secret Room
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
        "You are in front of an abandoned house, late on Halloween night. " +
        "You went there looking for your friends who ran off ahead of you.\n" +
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
    print("       Secret Room --- Kitchen -------- Foyer ------- Dining Room       ")
    print("                                                                        ")
    print("     ==============================================================     ")
    print("\nYou are currently at the " + Player1.location.name + ".")


# Initiates game sequence
def playGame():
    if Player1.location.wasVisited:
        print("\nYou are at the " + Player1.location.shortDes + "\n")
        print("=================================================\n")
    else:
        print("\n" + Player1.location.longDes + "\n")
        print("=================================================\n")
        Player1.location.wasVisited = True
    getInput()


# Moves player around game world based on user input
def getInput():
    global doorUnlocked
    North = 0
    South = 1
    East = 2
    West = 3
    Command = input("Please input a command: ")

    try:
        Command = Command.lower().rsplit(" ")
    except IndexError:
        Command = Command.lower()

    print()
    if Command[0] == 'north' or Command[0] == 'south' or Command[0] == 'east' or Command[0] == 'west':
        if Command[0] == 'north':
            Player.moveTo(Player1, Player1.location, North)
            if not Player1.location.wasVisited:
                Player.addScore(Player1)
            Player.addMove(Player1)
            playGame()

        if Command[0] == 'south':
            Player.moveTo(Player1, Player1.location, South)
            if not Player1.location.wasVisited:
                Player.addScore(Player1)
            Player.addMove(Player1)
            playGame()

        if Command[0] == 'east':
            Player.moveTo(Player1, Player1.location, East)
            if not Player1.location.wasVisited:
                Player.addScore(Player1)
            Player.addMove(Player1)
            playGame()

        if Command[0] == 'west':
            if Player1.location.value == 7:
                if doorUnlocked:
                    Player.moveTo(Player1, Player1.location, West)
                    if not Player1.location.wasVisited:
                        Player.addScore(Player1)
                        Player.addMove(Player1)
                else:
                    print("The door is locked.")
                    print("\n=================================================\n")
                    getInput()
            else:
                Player.moveTo(Player1, Player1.location, West)
                if not Player1.location.wasVisited:
                    Player.addScore(Player1)
                    Player.addMove(Player1)
            playGame()

    elif Command[0] == 'build':
        try:
            if Command[1] == 'key':
                if 'key putty' in Player1.inventory and 'key mold' in Player1.inventory:
                    Player1.inventory.append('key')
                    Player1.inventory.remove('key putty')
                    Player1.inventory.remove('key mold')
                    print("\nYour inventory is now: " + str(Player1.inventory))
                else:
                    print("\nYou don't have the correct items to build this.")
            else:
                print("\nYou can't build that.")
            print("\n=================================================\n")
            getInput()
        except IndexError:
            print("Please use 'build' plus two items you'd like to combine.")
            print("\n=================================================\n")
            getInput()

    elif Command[0] == 'unlock':
        try:
            if Command[1]:
                if Command[1] == 'door':
                    if 'key' in Player1.inventory:
                        if Player1.location.value == 7:
                            doorUnlocked = True
                            Player1.inventory.remove('key')
                            print("\nYou unlocked the door.")
                            print("\n=================================================\n")
                        else:
                            print("\nThat doesn't work here")
                            print("\n=================================================\n")
                    else:
                        print("\nYou have nothing to unlock it with.")
                        print("\n=================================================\n")
                else:
                    print("\nYou can't unlock that.")
                    print("\n=================================================\n")
                getInput()
        except IndexError:
            print("\nPlease enter 'unlock' + the item you would like to unlock.")
            print("\n=================================================\n")
            getInput()

    elif Command[0] == 'use':
        try:
            if Command[1]:
                if Command[1] in Player1.inventory:
                    if Command[1] == 'radio':
                        if Player1.location.value == 11:
                            endWin()
                            playAgain()
                        else:
                            endLose()
                            playAgain()
                    else:
                        print("\nYou don't know if you can use this here.")
                        print("\n=================================================\n")
                        getInput()
                else:
                    print("This item is not in your inventory")
                    print("\n=================================================\n")
                getInput()
        except IndexError:
            print("\nPlease enter 'use' + the item you would like to use.")
            print("\n=================================================\n")
            getInput()

    elif Command[0] == 'drop':
        try:
            if Command[1]:
                if Command[1] in Player1.inventory:
                    Player.dropItem(Player1, Command[1])
                playGame()
        except IndexError:
            print("\nPlease enter 'drop' + the item you would like to drop.")
            print("\n=================================================\n")
            getInput()

    elif Command[0] == 'search':
        print(Player.locSearch(Player1, Player1.location))
        print("\n=================================================\n")
        getInput()

    elif Command[0] == 'inventory':  # Shows the player's inventory
        print(Player.showInventory(Player1))
        print("\n=================================================\n")
        getInput()

    elif Command[0] == 'take':
        try:
            if Command[1]:
                try:
                    # Support for taking the new items 'key putty' and 'key mold'
                    if Command[2]:
                        cmd1 = [Command[1], Command[2]]
                        cmd1 = ' '.join(cmd1)
                        if cmd1 in Player1.location.items:
                            if Player1.location.wasSearched:
                                Player1.inventory.append(cmd1)
                                Player1.location.items.remove(cmd1)
                                Player1.location.items = None
                                print("\nYour inventory is now: " + str(Player1.inventory))
                            else:
                                print("You don't know that is there.")
                        else:
                            print("That item is not here.")
                        # If the player has the items to build a key,
                        # tells the user that they are able to build the key
                        if cmd1 == 'key mold' and 'key putty' in Player1.inventory:
                            print("\nYou are now able to build a key!")
                        elif cmd1 == 'key putty' and 'key mold' in Player1.inventory:
                            print("\nYou are now able to build a key!")
                # Used if player is not taking 'key putty' or 'key mold'
                except IndexError:
                    if Command[1] in Player1.location.items:
                        if Player1.location.wasSearched:
                            Player1.inventory.append(Command[1])
                            Player1.location.items.remove(Command[1])
                            Player1.location.items = None
                            print("\nYour inventory is now: " + str(Player1.inventory))
                        else:
                            print("You don't know that is there.")
                    else:
                        print("That item is not here.")
            print("\n=================================================\n")
            getInput()
        except IndexError:
            print("\nPlease enter 'take' + the item you would like to take.")
            print("\n=================================================\n")
            getInput()
        except TypeError:
            print("\nThere are no items at this location.")
            print("\n=================================================\n")
            getInput()

    elif Command[0] == 'map':  # Shows the map if the player has it in their inventory
        if 'map' in Player1.inventory:
            showMap()
            input("\nPress <Enter> to continue")
            print("\n=================================================\n")
        else:
            print("You have no map to look at.")
            print("\n=================================================\n")
        getInput()

    elif Command[0] == 'help':
        print("List of commands:\nNorth, South, East, West, Help, Quit," +
              "\nPoints, Map, Look, Search, Take, Use, Unlock, Build, Inventory and Drop.")
        print("\n=================================================\n")
        getInput()

    elif Command[0] == 'look':  # Shows the long description of the current location
        print(Player1.location.longDes)
        print("\n=================================================\n")
        getInput()

    elif Command[0] == 'points':  # Shows the player's score
        print("Your score is", Player1.score)
        print("\n=================================================\n")
        getInput()

    elif Command[0] == 'quit':
        print(endCredits)
        quit()

    else:
        print("Please input a valid command, or type 'help' to view a list of valid commands.")
        print("\n=================================================\n")
        getInput()


# Shows game win ending
def endWin():
    print(
        "\nYou turn on the radio safely in the secret room behind the fridge. " +
        "You call for help from anyone who's out there....\nLuckily for you, someone picks up and comes to save you.")


# Shows game lose ending
def endLose():
    print("\nYou turn on the radio and it makes a loud squawking. " +
          "You look around hoping nothing or no one heard it...\n" +
          "You turn around again and you come face to face with a gruesome looking clown....\n" +
          "\nHello " + Player1.name + ", it's time to float\" it says while dragging you towards the closet...")


def resetGame():
    resetPlayerData()
    resetLocationData()


def resetPlayerData():
    Player1.name = ""
    Player1.score = 0
    Player1.location = None
    Player1.moveCount = 0
    Player1.inventory = []


def resetLocationData():
    Locations = [pStart, Kitchen, DiningRoom, Hallway, SecretRoom, Bathroom,
                 FamilyRoom, Bedroom, Window, Porch, Closet, HiddenRoom]
    for i in Locations:
        i.wasVisited = False
        i.wasSearched = False
    # <editor-fold desc="Item reset">
    pStart.items = [None]
    Kitchen.items = ['knife']
    DiningRoom.items = [None]
    Hallway.items = ['map']
    SecretRoom.items = [None]
    Bathroom.items = ['key putty']
    FamilyRoom.items = ['key mold']
    Bedroom.items = [None]
    Window.items = [None]
    Porch.items = ['flashlight']
    Closet.items = ['balloon']
    HiddenRoom.items = ['radio']
    # </editor-fold>


def playAgain():
    global doorUnlocked
    print("\n=================================================\n")
    cmd = str(input("Would you like to play again(yes/no)? ")).lower()
    if cmd == 'yes':
        resetGame()
        doorUnlocked = False
        print("\n=================================================\n")
        main()
    else:
        print(endCredits)
        quit()


def main():
    startProgram()
    Player1.location = pStart
    playGame()


main()
