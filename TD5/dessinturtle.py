import turtle as t
import os

def drawsquare(nombre) :
    n = 0
    t.color('red')
    while n < nombre :
        for i in range(4) :
            t.pendown()
            t.forward(25)
            t.left(90)
        t.penup()

        t.forward(30)
        n+=1


def forme(cotes, longueur, nombre) :
    angle = 360/cotes
    n = 0
    t.color('red')

    while n < nombre :
        for i in range(cotes) :
            t.pendown()
            t.forward(longueur)
            t.left(angle)
        t.penup()

        t.forward(longueur + 5)
        n+=1


def etoile(longueur) :
    forme(3, longueur, 1)

    t.penup()
    t.left(360/3)
    t.forward(longueur/3)
    t.pendown()
    t.right(60)
    t.forward(longueur/3)

    for i in range(3) :
        t.left(360/3)
        t.forward(longueur)

if __name__ == '__main__' :
    #cotes = input('cotés')
    #longueur = input('longueur')
    #nombre = input('nombre')

    #forme(int(cotes), int(longueur), int(nombre))
    etoile(300)
