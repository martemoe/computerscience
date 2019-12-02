#A text space adventure game

from graphics import*
import time

win = GraphWin("Text Adventure", 1200, 700)
win.setBackground("Black")
win.setCoords(0.0,0.0,10.0,10.0)

def clear(background):
    x = Rectangle(Point(0,0),Point(10,10))
    x.setFill(background)
    x.draw(win)

def textline1extra(*sentence):
    " ".join(sentence)
    x = Text(Point(5,9.5), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)

def textline1(sentence):
    " ".join(sentence)
    x = Text(Point(5,9.5), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)

def textline2(sentence):
    " ".join(sentence)
    x = Text(Point(5,9), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)

def textline3(sentence):
    " ".join(sentence)
    x = Text(Point(5,8.5), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)

def textline4(sentence):
    " ".join(sentence)
    x = Text(Point(5,8), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)

def textline5(sentence):
    " ".join(sentence)
    x = Text(Point(5,7.5), n)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)


def textline6(sentence):
    x = Text(Point(5,7), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)


def textline8(sentence):
    x = Text(Point(5,6), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)

def textline9(sentence):
    x = Text(Point(5,3), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    time.sleep(3)

def twoopt(opt1,opt2):
    one = Text(Point(2.5,5), opt1)
    one.setSize(18)
    one.setFill("White")
    one.draw(win)
    x = len(opt1)
    boxone = Rectangle(Point(2.5-(x/2)*0.1,5.25),Point(2.5+(x/2)*0.1,4.75))
    boxone.setOutline("White")
    boxone.draw(win)
    two = Text(Point(7.5,5), opt2)
    two.setSize(18)
    two.setFill("White")
    two.draw(win)
    y = len(opt2)
    boxtwo = Rectangle(Point(7.5-(y/2)*0.1,5.25),Point(7.5+(y/2)*0.1,4.75))
    boxtwo.setOutline("White")
    boxtwo.draw(win)
    
def threeoptions(opt1,opt2,opt3):
    one = Text(Point(2.5,5), opt1)
    one.setSize(18)
    one.setFill("White")
    one.draw(win)
    x = len(opt1)
    boxone = Rectangle(Point(2.5-(x/2)*0.1,5.25),Point(2.5+(x/2)*0.1,4.75))
    boxone.setOutline("White")
    boxone.draw(win)
    two = Text(Point(5,5), opt2)
    two.setSize(18)
    two.setFill("White")
    two.draw(win)
    y = len(opt2)
    boxtwo = Rectangle(Point(5-(y/2)*0.1,5.25),Point(5+(y/2)*0.1,4.75))
    boxtwo.setOutline("White")
    boxtwo.draw(win)
    three = Text(Point(7.5,5), opt3)
    three.setSize(18)
    three.setFill("White")
    three.draw(win)
    z = len(opt3)
    boxthree = Rectangle(Point(7.5-(z/2)*0.1,5.25),Point(7.5+(z/2)*0.1,4.75))
    boxthree.setOutline("White")
    boxthree.draw(win)

    

def fouroptions(opt1,opt2,opt3,opt4):
    one = Text(Point(2,5), opt1)
    one.setSize(18)
    one.setFill("White")
    one.draw(win)
    x = len(opt1)
    boxone = Rectangle(Point(2-(x/2)*0.1,5.25),Point(2+(x/2)*0.1,4.75))
    boxone.setOutline("White")
    boxone.draw(win)
    two = Text(Point(4,5), opt2)
    two.setSize(18)
    two.setFill("White")
    two.draw(win)
    y = len(opt2)
    boxtwo = Rectangle(Point(4-(y/2)*0.1,5.25),Point(4+(y/2)*0.1,4.75))
    boxtwo.setOutline("White")
    boxtwo.draw(win)
    three = Text(Point(6,5), opt3)
    three.setSize(18)
    three.setFill("White")
    three.draw(win)
    z = len(opt3)
    boxthree = Rectangle(Point(6-(z/2)*0.1,5.25),Point(6+(z/2)*0.1,4.75))
    boxhree.setOutline("White")
    boxthree.draw(win)
    four = Text(Point(8,5), opt4)
    four.setSize(18)
    four.setFill("White")
    four.draw(win)
    w = len(opt3)
    boxfour = Rectangle(Point(8-(w/2)*0.1,5.25),Point(8+(w/2)*0.1,4.75))
    boxfour.setOutline("White")
    boxfour.draw(win)

    
#The intro for the game
def main():
    win = GraphWin("Text Adventure", 1200, 700)
    win.setBackground("Black")
    win.setCoords(0.0,0.0,10.0,10.0)
    textline2("Once upon a time a long time ago, magic was still an ordinary part of the world along with all the creatures it that came with.")
    textline3("Humankind lived in harmony with all these creatures. That was until the dark wizard Alatar stole the Cup of Life.")
    textline4("The Cup of Life is what gives The Great Forest life, and now the forest is slowly dying.")
    clear("Black")
    win.setBackground("Black")
    textline2("Hello, I am the All Knowing. I will be guiding you throug this adventure.")
    textline4("Please let me know your name!")
    nameentry = Entry(Point(5,6), 10)
    nameentry.draw(win)
    textline9("*Click anywhere to continue*")
    win.getMouse()
    name = nameentry.getText()
    clear("Black")
    nameentry.undraw()
    textline1extra("Hello", name)
    choosecharacter()
    #Add more here


#Choose character
def choosecharacter():
    clear("Black")
    textline2("Now it is time for you to decide what character you want to be. Each character has its own special skillset that will help you.")
    textline3("All of the characters are able to complete the mission, as long as you make the right decision.")
    textline4("Now choose wisely!")
    threeoptions("The Great Wizard", "The young Elf Prince(ss)", "The Master Spy")
    o = win.getMouse()
    boxone = Rectangle(Point(2.5-((len("The Great Wizard"))/2)*0.1,5.25),Point(2.5+((len("The Great Wizard"))/2)*0.1,4.75))
    P11 = boxone.getP1()
    P21 = boxone.getP2()
    boxtwo = Rectangle(Point(5-((len("The young Elf Prince(ss)"))/2)*0.1,5.25),Point(5+((len("The young Elf Prince"))/2)*0.1,4.75))
    P12 = boxtwo.getP1()
    P22 = boxtwo.getP2()
    boxthree = Rectangle(Point(7.5-((len("The Master Spy"))/2)*0.1,5.25),Point(7.5+((len("The Master Spy"))/2)*0.1,4.75))
    P13 = boxthree.getP1()
    P23 = boxthree.getP2()
    if P11.getX()< o.getX()<P21.getX() and P11.getY()> o.getY()>P21.getY():
        clear("Black")
        textline1extra("Hello, Great Wizard", name)
        textline2("Let's get to saving the world right away!")
        character = "Great Wizard"
        charactername = ("Great wizard", name)
    elif P12.getX()< o.getX()<P22.getX() and P12.getY()> o.getY()>P22.getY():
        clear("Black")
        textline1extra("Hello, young Elf prince(ss)", name)
        textline2("Let's get to saving the world right away!")
        character = "young elf prince(ss)"
        charactername = ("young elf prince(ss)", name)
    elif P13.getX()< o.getX()<P23.getX() and P13.getY()> o.getY()>P23.getY():
        clear("Black")
        textline1extra("Hello, Master Spy", name)
        textline2("Let's get to saving the world right away!")
        character = "Master Spy"
        charactername = ("Master Spy", name)
    else:
        textline9("Please press one of the options")
    edgeofforest()

#The beggining of the game and the "return" point when leaving a place
def edgeofforest():
    clear("Black")
    textline4("You are currently at the edge of the The Great Forest. You have to decide where you want to go next...")
    textline6("Do you wish to go to:")
    threeoptions("The Tavern", "The Forest", "The Store")
    o = win.getMouse()
    boxone = Rectangle(Point(2.5-((len("The Tavern"))/2)*0.1,5.25),Point(2.5+((len("The Tavern"))/2)*0.1,4.75))
    P11 = boxone.getP1()
    P21 = boxone.getP2()
    boxtwo = Rectangle(Point(5-((len("The Forest"))/2)*0.1,5.25),Point(5+((len("The Forest"))/2)*0.1,4.75))
    P12 = boxtwo.getP1()
    P22 = boxtwo.getP2()
    boxthree = Rectangle(Point(7.5-((len("The Store"))/2)*0.1,5.25),Point(7.5+((len("The Store"))/2)*0.1,4.75))
    P13 = boxthree.getP1()
    P23 = boxthree.getP2()
    if P11.getX()< o.getX()<P21.getX() and P11.getY()> o.getY()>P21.getY():
        tavern()
    elif P12.getX()< o.getX()<P22.getX() and P12.getY()> o.getY()>P22.getY():
        forest()
    elif P13.getX()< o.getX()<P23.getX() and P13.getY()> o.getY()>P23.getY():
        store()
    else:
        textline9("The option was not accepted, please choose an action")
        edgeofforest()


def tavern():
    clear("Black")
    textline1extra("\"Hello! I am the owner of this fine establishment! What can I possibly help you with\"")
    threeoptions("Gather information", "Get a drink", "Leave")
    o = win.getMouse()
    boxone = Rectangle(Point(2.5-((len("Gather information"))/2)*0.1,5.25),Point(2.5+((len("Gather information"))/2)*0.1,4.75))
    P11 = boxone.getP1()
    P21 = boxone.getP2()
    boxtwo = Rectangle(Point(5-((len("Get a drink"))/2)*0.1,5.25),Point(5+((len("Get a drink"))/2)*0.1,4.75))
    P12 = boxtwo.getP1()
    P22 = boxtwo.getP2()
    boxthree = Rectangle(Point(7.5-((len("Leave"))/2)*0.1,5.25),Point(7.5+((len("Leave"))/2)*0.1,4.75))
    P13 = boxthree.getP1()
    P23 = boxthree.getP2()
    if P11.getX()< o.getX()<P21.getX() and P11.getY()> o.getY()>P21.getY():
        clear("Black")
        textline2("\"Information? Of course I have information! You are looking at the most informed creature in the world!! As a tavern owner I get all the gossip from all")
        textline3("corners of the world. Now what is it that you want to know?\"")
    elif P12.getX()< o.getX()<P22.getX() and P12.getY()> o.getY()>P22.getY():
        clear("Black")
        textline2("\"Ah I see; you want a refresher! Well ofcourse, I have the most delicious Ale ever made! People come from far and wide to get a taste of it!\"")
    elif P13.getX()< o.getX()<P23.getX() and P13.getY()> o.getY()>P23.getY():
        clear("Black")
        textline2("\" Leave? Already? Well I guess I will have to let you go...\"")
        textline3("\" But if you ever want to come by to have a chat or get a drink, I will be here\"")
        clear("Black")
        textline4("Heading back to the edge of the forest")
        edgeofforest()
    else:
        textline9("The option was not accepted, please choose an action")
        tavern()

def forest():
    clear("Black")
    textline2("You are heading deep into the forest. It is stil beautiful, but you can feel that it is slowly dying.")
    textline3("You approach a crossroad, you will have to decide which way to go from here!")
    fouroptions("The dark forest path", "The cave", "The cabin in the woods", "Turn back") 
    o = win.getMouse()
    boxone = Rectangle(Point(2.5-((len("The dark forest path"))/2)*0.1,5.25),Point(2.5+((len("The dark forest path"))/2)*0.1,4.75))
    P11 = boxone.getP1()
    P21 = boxone.getP2()
    boxtwo = Rectangle(Point(5-((len("The cave"))/2)*0.1,5.25),Point(5+((len("The cave"))/2)*0.1,4.75))
    P12 = boxtwo.getP1()
    P22 = boxtwo.getP2()
    boxthree = Rectangle(Point(7.5-((len("The cabin in the woods"))/2)*0.1,5.25),Point(7.5+((len("The cabin in the woods"))/2)*0.1,4.75))
    P13 = boxthree.getP1()
    P23 = boxthree.getP2()
    boxfour = Rectangle(Point(8-((len("Turn back"))/2)*0.1,5.25),Point(8+((len("Turn back"))/2)*0.1,4.75))
    P14 = boxfour.getP1()
    P24 = boxfour.getP1()
    if P11.getX()< o.getX()<P21.getX() and P11.getY()> o.getY()>P21.getY():
        clear("Black")
        textline2("You walk deeper into the forest. The heavy growth of trees is blocking out the sunlight!")
        if character == "young elf prince(ss)":
            textline3("This is no place for an elf! The elves can only thrive in places with plenty of sunlight.Turn back now, before you get lost in the forest!")
            textline4("Turn back?")
            twooptions("YES","NO")
            o = win.getMouse()
            boxone = Rectangle(Point(2.5-((len("YES"))/2)*0.1,5.25),Point(2.5+((len("YES"))/2)*0.1,4.75))
            P11 = boxone.getP1()
            P21 = boxone.getP2()
            boxtwo = Rectangle(Point(5-((len("NO"))/2)*0.1,5.25),Point(5+((len("NO"))/2)*0.1,4.75))
            P12 = boxtwo.getP1()
            P22 = boxtwo.getP2()
            if P11.getX()< o.getX()<P21.getX() and P11.getY()> o.getY()>P21.getY():
                textline2("You are heading back to the crossroads...")
                forest()
            elif P12.getX()< o.getX()<P22.getX() and P12.getY()> o.getY()>P22.getY():
                textline2("You are walking deeper into the forest and getting lost. It's so dark now that you can't even see what the creatures in the dark approach you")
                textline3("You fight them bravely, but the fact that you can't see them makes it impossible to win.")
                lose("the creatures hiding in the shadow")
        elif character == "Great Wizard":
            textline2("")
    elif P12.getX()< o.getX()<P22.getX() and P12.getY()> o.getY()>P22.getY():
        clear("Black")
    elif P13.getX()< o.getX()<P23.getX() and P13.getY()> o.getY()>P23.getY():
        clear("Black")
    elif P14.getX()< o.getX()<P24.getX() and P14.getY()> o.getY()>P24.getY():
        clear("Black")
    else:
        textline9("The option was not accepted, please choose an action")
        forest()



def store():
    clear("Black")
    textline2("Hello! Welcome to the store. Here you can buy ")


def win():
    textline1extra("Congratulations", charactername)
    textline2("you were successfull in saving the world from the Evil Wizard Alatar!")
    textline3("The Cup of life has been returned to its rightful place, and the world can continue on as it has been.")
    textline4("Thank you for playing this game!")

def lose(enemy):
    textline1extra("Oh no! you have fallen by the hands of", enemy)
    textline2("You were unfortunatly unsuccessful in completing the advenure...")
    textline3("Would you like to play agin?")
    twooptions("YES","NO")
    o = win.getMouse()
    boxone = Rectangle(Point(2.5-((len("YES"))/2)*0.1,5.25),Point(2.5+((len("YES"))/2)*0.1,4.75))
    P11 = boxone.getP1()
    P21 = boxone.getP2()
    boxtwo = Rectangle(Point(5-((len("NO"))/2)*0.1,5.25),Point(5+((len("NO"))/2)*0.1,4.75))
    P12 = boxtwo.getP1()
    P22 = boxtwo.getP2()
    if P11.getX()< o.getX()<P21.getX() and P11.getY()> o.getY()>P21.getY():
        clear("Black")
        textline2("Thank you for playing again! Now I will take you back to the edge of the forest!")
        egeofforest()
    elif P12.getX()< o.getX()<P22.getX() and P12.getY()> o.getY()>P22.getY():
        clear("Black")
        textline2("Oh, okay, if thet is what you want...")
        textline3("Goodbye for now...")


if __name__ == '__main__':
    main()


