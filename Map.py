##Map.py
##Author: David Siegel

from graphics import *

def main():
    win = GraphWin("Game World Map", 551, 551)

    ##Outer Boundary
    rect = Rectangle(Point(10, 10), Point(540, 540))
    rect.draw(win)

    ##Closet Area
    rect = Rectangle(Point(10, 10), Point(188, 188))
    rect.draw(win)

    ##Window Area
    rect = Rectangle(Point(188, 10), Point(362, 188))
    rect.draw(win)

    ##Porch Area
    rect = Rectangle(Point(362, 10), Point(540, 188))
    rect.draw(win)

    ##Family Room
    rect = Rectangle(Point(10, 188), Point(188, 362))
    rect.draw(win)

    ##Hallway
    rect = Rectangle(Point(188, 188), Point(362, 362))
    rect.draw(win)

    ##Bathroom
    rect = Rectangle(Point(362, 188), Point(540, 362))
    rect.draw(win)

    ##Kitchen
    rect = Rectangle(Point(10, 362), Point(188, 540))
    rect.draw(win)

    ##Foyer
    rect = Rectangle(Point(188, 362), Point(362, 540))
    rect.draw(win)

    ##DiningRoom
    rect = Rectangle(Point(362, 362), Point(540, 540))
    rect.draw(win)

        
main()
