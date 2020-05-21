import turtle as t

def triangle_equilateral(cote, color, angle = 360/3) :
    """Dessine un triangle équilatéral de coté donné et de couleur donnée
    cote : int ou float
    couleur : str
    angle : par défaut 360/3, pour obtenir un triangle, ne pas le changer"""
    t.begin_poly()
    for n in range(3) :
        t.fillcolor(color)
        t.pendown()
        t.forward(cote)
        t.right(angle)

    t.left(angle)
    t.end_poly()

    poly = t.get_poly()
    return(poly)

def drawstarline(longueur, nb) :
    """Permet de dessiner les 6 traits partant du centre"""
    angle = 360/nb
    for a in range(nb) :
        t.goto(0, 0)
        t.color('black')
        t.forward(longueur)
        t.right(angle)


def draw_figure() :
    """Fonction finale pour le dessin de la figure entière."""
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
            color = '#6e6eff'
        else :
            color = '#ffcd00'

        t.begin_fill()
        triangle_equilateral(250, color)
        t.end_fill()

        #Placement au bon point de départ pour le prochain triangle
        t.right(180)
        t.forward(250)



    drawstarline(500, 6)
    t.done()
