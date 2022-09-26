import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup() 
t.goto(100, 100)  
t.write("두 수 모두 양수.")
t.goto(-100, 100)
t.write("첫번째 수만 음수.")
t.goto(-100, -100)
t.write("두 수 모두 음수.")
t.goto(100, -100)
t.write("두번째 수만 음수")

t.goto(0,0)
t.pendown()

a1 = turtle.textinput("", "첫번째 숫자를 입력하시오: ")
a2 = turtle.textinput("", "두번째 숫자를 입력하시오: ")

if a1 * a2 > 0:
    if a1 > 0:
        t.goto(100,100)
    else:
        t.goto(-100,-100)
if a1 * a2 <0:
    if a1>0:
        t.goto(100,-100)
    else:
        t.goto(-100,-100)