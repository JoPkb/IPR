import turtle as t

#exercice 3
def drawforme(anglestart, cotes, longueur, nombre, couleur) :

    angle = 360/cotes
    n = 0
    t.color(couleur)

    while n < nombre :
        for i in range(cotes) :
            t.pendown()
            t.forward(longueur)
            t.right(angle)

        n+=1

def drawstar(anglestart, longueur, nombre, couleur) :

    for i in range(nombre) :

        drawforme(anglestart, 3, longueur, 1, couleur)

        t.penup()
        t.forward(longueur/3)
        t.left(60)
        t.forward(longueur/3)
        t.right(120)
        t.pendown()

        drawforme(180, 3, longueur,1,  couleur)
        t.left(360/3)

        # t.penup()
        # t.right(360/3)
        # t.forward(longueur/3 )
        # t.pendown()
        # t.left(60)
        # t.forward(longueur/3)
        #
        # for i in range(3) :
        #     t.right(360/3)
        #     t.forward(longueur)

def drawchaine(deltaangle, deltataille, couleur1, couleur2, nombre) :
    taille = 10
    angle = 0
    n = 0
    while n < nombre :
        drawforme(angle, 4, taille, 1, couleur1)
        t.penup()
        t.forward(taille*2)
        t.pendown()
        drawstar(angle, taille, 1, couleur2)
        t.penup()
        t.forward(taille*2)

        taille += deltataille

        n+=1



if __name__ =='__main__' :
    #drawstar(0, 500, 1, 'red')
    drawchaine(60, 5, 'red', 'blue', 60)
