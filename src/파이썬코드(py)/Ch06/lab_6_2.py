import turtle

t = turtle.Turtle()

def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360 // n)  

for i in range(20):
    t.left(30)
    n_polygon(4, 100)
turtle.done()