##CMPT Semester Project
##Author: David Siegel
##Version: 0.1

def main():
    main.playerScore = 0
    playerName = input("What is your name?")
    print("Hello " + playerName + "! Welcome to It Part 2!")
    def showScore():
        print("Your score is", main.playerScore)
    showScore()
    playerLocation = "You are outside an abandoned house, late on Halloween night. You went there looking for your friends who ran off ahead of you."
    print(playerLocation)
    
    def pressEnter():
        input("Press Enter to continue")
        main.playerScore = main.playerScore + 5
        print("=================================================")
        showScore()
        print("")
        
    pressEnter()
    
    print("You move to the front door and try to open it...")
    print("The door opens and you walk into a dark, dingy main foyer. You see stairs leading upstairs to your left.")
    print("Around the corner to your right, you see stairs leading down to the basement.")
    pressEnter()
    
    print("You turn left and go uptstairs. The stairs creak as you walk up them")
    print("When you reach the top of the stairs, you see 3 doors going down the hall; 2 on your left, 1 on your right.")
    print("As you try the first door on your left, you hear a scream from the basement....")
    pressEnter()

    
main()
