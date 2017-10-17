##Map.py
##Author: David Siegel

from graphics import *

def main():
    win = GraphWin("Game World Map", 550, 550)
    rect = Rectangle(Point(10, 10), Point(539, 539))
    rect.draw(win)

main()
