import turtle as t

def triangle_equilateral(cote, couleur, angle = 360/3) :
    """Dessine un triangle équilatéral de coté donné et de couleur donnée
    cote : int ou float
    couleur : str
    angle : par défaut 360/3, pour obtenir un triangle, ne pas le changer"""

    # t.fillcolor('red')
    # t.begin_fill()
    for n in range(3) :
        t.pendown()
        t.color(couleur)
        t.forward(cote)
        t.right(angle)

    t.left(angle)
    

def drawstarline(longueur, nb) :
    angle = 360/nb
    for a in range(nb) :
        t.goto(0, 0)
        t.color('black')
        t.forward(longueur)
        t.right(angle)
