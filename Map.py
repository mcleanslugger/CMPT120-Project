##Map.py
##Author: David Siegel

from graphics import *

def showMap():
    win = GraphWin("Game World Map", 551, 551)

    ##Outer Boundary
    rect = Rectangle(Point(10, 10), Point(540, 540))
    rect.setWidth(2)
    rect.draw(win)



    ##Closet Area
    southLine = Line(Point(10, 188), Point(188, 188))
    southLine.setWidth(2)
    eastLine1 = Line(Point(188, 10), Point(188, 69))
    eastLine1.setWidth(2)
    eastLine2 = Line(Point(188, 129), Point(188, 188))
    eastLine2.setWidth(2)
    southLine.draw(win)
    eastLine1.draw(win)
    eastLine2.draw(win)

    closetCenter = Point(89, 89)
    Closet = Text(closetCenter, "Closet")
    Closet.draw(win)


    ##Window Area
    southLine1 = Line(Point(188, 188), Point(246, 188))
    southLine1.setWidth(2)
    southLine2 = Line(Point(304, 188), Point(362, 188))
    southLine2.setWidth(2)
    southLine1.draw(win)
    southLine2.draw(win)

    windowCenter = Point(275, 89)
    Window = Text(windowCenter, "Window")
    Window.draw(win)



    ##Porch Area
    westLine1 = Line(Point(362, 10), Point(362, 69))
    westLine1.setWidth(2)
    westLine2 = Line(Point(362, 129), Point(362, 188))
    westLine2.setWidth(2)
    southLine = Line(Point(362, 188), Point(540, 188))
    southLine.setWidth(2)
    westLine1.draw(win)
    westLine2.draw(win)
    southLine.draw(win)

    porchCenter = Point(451, 89)
    Porch = Text(porchCenter, "Porch")
    Porch.draw(win)



    ##Family Room
    eastLine1 = Line(Point(188, 188), Point(188, 246))
    eastLine1.setWidth(2)
    eastLine2 = Line(Point(188, 304), Point(188, 362))
    eastLine2.setWidth(2)
    southLine = Line(Point(10, 362), Point(188, 362))
    southLine.setWidth(2)
    eastLine1.draw(win)
    eastLine2.draw(win)
    southLine.draw(win)

    familyCenter = Point(89, 275)
    FamilyRoom = Text(familyCenter, "Family Room")
    FamilyRoom.draw(win)



    ##Hallway
    hallwayCenter = Point(275, 275)
    Hallway = Text(hallwayCenter, "Hallway")
    Hallway.draw(win)



    ##Bathroom
    westLine1 = Line(Point(362, 188), Point(362, 246))
    westLine1.setWidth(2)
    westLine2 = Line(Point(362, 304), Point(362, 362))
    westLine2.setWidth(2)
    southLine = Line(Point(362, 362), Point(540, 362))
    southLine.setWidth(2)
    westLine1.draw(win)
    westLine2.draw(win)
    southLine.draw(win)

    bathroomCenter = Point(451, 275)
    Bathroom = Text(bathroomCenter, "Bathroom")
    Bathroom.draw(win)



    ##Kitchen
    eastLine1 = Line(Point(188, 362), Point(188, 421))
    eastLine1.setWidth(2)
    eastLine2 = Line(Point(188, 481), Point(188, 540))
    eastLine2.setWidth(2)
    eastLine1.draw(win)
    eastLine2.draw(win)

    kitchenCenter = Point(89, 451)
    Kitchen = Text(kitchenCenter, "Kitchen")
    Kitchen.draw(win)



    ##Foyer
    northWall1 = Line(Point(188, 362), Point(246, 362))
    northWall1.setWidth(2)
    northWall2 = Line(Point(304, 362), Point(362, 362))
    northWall2.setWidth(2)
    northWall1.draw(win)
    northWall2.draw(win)

    foyerCenter = Point(275, 451)
    Foyer = Text(foyerCenter, "Foyer")
    Foyer.draw(win)


    ##Dining Room
    westWall1 = Line(Point(362, 362), Point(362, 421))
    westWall1.setWidth(2)
    westWall2 = Line(Point(362, 481), Point(362, 540))
    westWall2.setWidth(2)
    westWall1.draw(win)
    westWall2.draw(win)

    diningrmCenter = Point(451, 451)
    DiningRoom = Text(diningrmCenter, "Dining Room")
    DiningRoom.draw(win)



    
showMap()
