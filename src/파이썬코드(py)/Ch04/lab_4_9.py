import turtle
t = turtle.Turtle() 
t.shape("turtle") 
 
s = turtle.textinput("", "도형을 입력하시오: ") 
if s == "사각형":
    s = turtle.textinput("", "가로: ")
    w = int(s) 
    s = turtle.textinput("", "세로: ")
    h = int(s) 
    t.forward(w) 
    t.left(90) 
    t.forward(h) 
    t.left(90) 
    t.forward(w) 
    t.left(90) 
    t.forward(h)
if s =="원":
    s = turtle.textinput("", "반지름: ")
    w = int(s)
    t.circle(w)
if s == "삼각형":
    s = turtle.textinput("", "길이: ")
    w = int(s)
    t.forward(w)
    t.left(60)
    t.forward(w)
    t.left(60)
    t.forward(w)


turtle.done()