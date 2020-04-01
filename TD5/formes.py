import turtle as t

#exercice 3
def drawforme(cotes, longueur, couleur) :

    angle = 360/cotes
    t.color(couleur)

    for i in range(cotes) :
        t.pendown()
        t.forward(longueur)
        t.right(angle)



def drawstar(longueur, nombre, couleur) :

    for i in range(nombre) :

        drawforme(3, longueur, couleur)

        t.penup()
        t.forward(longueur/3)
        t.left(60)
        t.forward(longueur/3)
        t.right(120)
        t.pendown()

        drawforme(3, longueur, couleur)
        #t.left(360/3)

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
        drawforme(4, taille, couleur1)
        t.penup()
        t.forward(taille*2)
        t.pendown()
        drawstar(taille, 1, couleur2)
        t.penup()
        t.forward(taille*2)

        taille += deltataille

        n+=1



if __name__ =='__main__' :
    #drawstar(100, 10, 'red')
    drawchaine(60, 5, 'red', 'blue', 15)
    t.done()
    #drawforme(4, 50, 'red')
