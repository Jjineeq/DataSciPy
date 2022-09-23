import turtle

def turtle_pic(n):
    import turtle
    t = turtle.Turtle()
    for i in range(n):
        t.forward(100)
        t.left(n/60)
    turtle.exitonclick()

turtle_pic(5)

