#A text space adventure game

from graphics import*
import time

win = GraphWin("Text Adventure", 1200, 700)
win.setBackground("Black")
win.setCoords(0.0,0.0,10.0,10.0)

def textline1(sentence):
    x = Text(Point(5,9.5), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)

def textline2(sentence):
    x = Text(Point(5,9), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)

def textline3(sentence):
    x = Text(Point(5,8.5), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)

def textline4(sentence):
    x = Text(Point(5,8), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)

def textline5(sentence):
    x = Text(Point(5,7.5), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)

def textline6(sentence):
    x = Text(Point(5,7), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)

def textline7(sentence):
    x = Text(Point(5,6.5), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)

def textline8(sentence):
    x = Text(Point(5,6), sentence)
    x.setSize(18)
    x.setFill("White")
    x.draw(win)
    
textline1("Once upon a time a long time ago, magic was still an ordinary part of the world along with all the creatures it that came with.")
textline2("Humankind lived in harmony with all these creatures. That was until the dark wizard Alatar stole the Cup of Life")
textline3("The Cup of Life is what gives")



