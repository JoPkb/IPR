from Formes import *
import turtle as t
from modiflist import *
#MENU :
choix = int(input('Entrez votre choix : 1 pour exercice 1, 2 pour exercice 2, etc... >>> '))

if choix == 1 :
    data = [1,1,1,2,3,10,10]

    print('liste comprimée :', comprime(data))
    print('liste comprimée et comptée:', compte(data))



elif choix == 2 :

    t.speed(20)
    for n in range(2) :
        for i in range(3) :
            triangle_equilateral(250, 'black')
        t.left(60)
    t.forward(250)
    t.right(60)

    #Dessin des 6 triangles entourant les 6 premiers.
    for a in range(6) :
        if a % 2 == 0 :
            color = '#8267E5'
        else :
            color = '#DEA759'

        t.begin_fill()
        triangle_equilateral(250, color)
        t.end_fill()

        #Placement au bon point de départ pour le prochain triangle
        t.right(180)
        t.forward(250)



    drawstarline(500, 6)
    t.done()
