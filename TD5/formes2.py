import turtle as t

def forme(taille, nbcote, col = 'red') :
    t.down()
    angle = 360/nbcote
    t.color(col)
    for i in range(nbcote) :
        t.forward(taille)
        t.right(angle)


def star(taille, col = 'red') :
    forme(taille, 3, col)

    t.penup()
    t.forward(taille/3)
    t.left(60)
    t.forward(taille/3)
    t.right(120)

    forme(taille, 3, col)

    t.done()
if __name__ == '__main__' :
    forme(20, 3)
