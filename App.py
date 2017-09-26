##CMPT Semester Project
##Author: David Siegel
##Version: 0.1

playerLocation = ""
playerName = input("What is your name? ")
playerScore = 0
playerLocationStart  = ("You are outside an abandoned house, late on Halloween night. "
                        "You went there looking for your friends who ran off ahead of you.")
playerLocation1      = ("You move to the front door and try to open it... "
                        "The door opens and you walk into a dark, dingy main foyer. "
                        "You see stairs leading upstairs to your left. Around the corner "
                        "to your right, you see stairs leading down to the basement.")
playerLocation2      = ("You turn left and go upstairs. The stairs creak as you walk up them. "
                        "When you reach the top of the stairs, you see 3 doors going down the hall; "
                        "2 on your left, 1 on your right. You open the first door on your left.")
playerLocation3      = ("The door is unlocked and you enter the room. It is completely empty except "
                        "for one picture on the wall facing the door. You move closer, and you see it's "
                        "a clown holding a red balloon, yet something is off about the clown. Just as you "
                        "are about to figure it out, a scream rings out from the basement...")
playerLocation4      = ("You rush down the satirs, nearly missing one and twisting your ankle. "
                        "As you near the door to the basement, you see a single red balloon floating in "
                        "front of the door. You try the door. It's locked. Just then you hear another "
                        "scream followed by silence. You turn around to find a clown behind you.\n"
                        "'Hello " + playerName + ", it's time to float.' the clown says laughing maniacally. "
                        "You try to run away but it grabs you and drags you downstairs...")

def main():
    startProgram()
    playGame()
    showCopyright()

def startProgram():
    global playerScore, playerLocation, playerLocationStart
        
    print("Hello " + playerName + "! Welcome to")
    print(" _____ _     _____           _     ___")
    print("|_   _| |   |  __ \         | |   |__ \ ")
    print("  | | | |_  | |__) |_ _ _ __| |_     ) |")
    print("  | | | __| |  ___/ _` | '__| __|   / / ")
    print(" _| |_| |_  | |  | (_| | |  | |_   / /_ ")
    print("|_____|\__| |_|   \__,_|_|   \__| |____|")
    print("\nBy: David Siegel\n")

def playGame():
    global playerScore, playerLocationStart, playerLocation, playerLocation1, playerLocation2, playerLocation3, playerLocation4

    while playerScore <= 20:
        changeLocation()
        playerScore += 5

def changeLocation():
    global playerScore, playerLocationStart, playerLocation, playerLocation1, playerLocation2, playerLocation3, playerLocation4
    
    print("Your score is", playerScore, "\n")
    if playerScore == 0:
        playerLocation = playerLocationStart
        print(playerLocation)
    elif playerScore == 5:
        playerLocation = playerLocation1
        print(playerLocation)
    elif playerScore == 10:
        playerLocation = playerLocation2
        print(playerLocation)
    elif playerScore == 15:
        playerLocation = playerLocation3
        print(playerLocation)
    elif playerScore == 20:
        playerLocation = playerLocation4
        print(playerLocation)
    else:
        return
    input("\nPress <Enter> to continue.")
    print("=================================================")

def showCopyright():
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")

main()
