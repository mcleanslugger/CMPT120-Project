##CMPT Semester Project
##Author: David Siegel
##Version: 0.1

playerLocation = ""
playerName = input("What is your name? ")
playerScore = 0

def main():
    main.playerLocationStart  = ("You are outside an abandoned house, late on Halloween night. "
                                 "You went there looking for your friends who ran off ahead of you.")
    main.playerLocation1      = ("You move to the front door and try to open it... "
                                 "The door opens and you walk into a dark, dingy main foyer. "
                                 "You see stairs leading upstairs to your left. Around the corner "
                                 "to your right, you see stairs leading down to the basement.")
    main.playerLocation2      = ("You turn left and go upstairs. The stairs creak as you walk up them. "
                                 "When you reach the top of the stairs, you see 3 doors going down the hall; "
                                 "2 on your left, 1 on your right. You open the first door on your left.")
    main.playerLocation3      = ("The door is unlocked and you enter the room. It is completely empty except "
                                 "for one picture on the wall facing the door. You move closer, and you see it's "
                                 "a clown holding a red balloon, yet something is off about the clown. Just as you "
                                 "are about to figure it out, a scream rings out from the basement...")
    main.playerLocation4      = ("You rush down the satirs, nearly missing one and twisting your ankle. "
                                 "As you near the door to the basement, you see a single red balloon floating in "
                                 "front of the door. You try the door. It's locked. Just then you hear another "
                                 "scream followed by silence. You turn around to find a clown behind you.\n"
                                 "'Hello " + playerName + ", it's time to float.' the clown says laughing maniacally. "
                                 "You try to run away but it grabs you and drags you downstairs...")
    startProgram()
    pressEnter()
    pressEnter()
    pressEnter()
    pressEnter()



def startProgram():
    print("Hello " + playerName + "! Welcome to\n")
    print(" _____ _     _____           _     ___")
    print("|_   _| |   |  __ \         | |   |__ \ ")
    print("  | | | |_  | |__) |_ _ _ __| |_     ) |")
    print("  | | | __| |  ___/ _` | '__| __|   / / ")
    print(" _| |_| |_  | |  | (_| | |  | |_   / /_ ")
    print("|_____|\__| |_|   \__,_|_|   \__| |____|")
    print("\nBy: David Siegel\n")
    showScore()
    global playerLocation
    playerLocation = main.playerLocationStart
    print(playerLocation)

def showCopyright():
    print("\nTHE END\n")
    print("(c) 2017 David Siegel, idruless@gmail.com")
        
def showScore():
    print("Your score is", playerScore, "\n")

def changeLocation():
    global playerLocation
    if playerScore == 5:
        playerLocation = main.playerLocation1
        print(playerLocation)
    elif playerScore == 10:
        playerLocation = main.playerLocation2
        print(playerLocation)
    elif playerScore == 15:
        playerLocation = main.playerLocation3
        print(playerLocation)
    elif playerScore == 20:
        playerLocation = main.playerLocation4
        print(playerLocation)
        showCopyright()
    else:
        return

def pressEnter():
    input("Press Enter to continue")
    global playerScore
    playerScore += 5
    print("=================================================")
    showScore()
    changeLocation()

main()
