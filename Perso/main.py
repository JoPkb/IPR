from Formes import *
import turtle as t

for n in range(2) :
    for i in range(3) :
        if n == 0 :
            triangle_equilateral(250,'black')
        elif n == 1 :
            triangle_equilateral(250, 'black')
    t.left(60)
t.forward(250)
t.right(60)

for a in range(6) :
    if a % 2 == 0 :
        t.fillcolor('yellow')
        t.color('yellow')
    else :
        t.fillcolor('purple')
        t.color('purple')
    t.begin_fill()
    t.forward(250)
    t.right(120)
    t.forward(250)
    t.right(120)
    t.forward(250)
    t.end_fill()
    t.right(180)
    t.forward(250)



drawstarline(500, 6)
t.done()
