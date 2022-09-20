import turtle
# 1.2 (1)
t = turtle.Turtle()
t.shape('turtle')
t.forward(120) # 120pixel만큼 전진
t.left(120) # 120도 회전
t.forward(120)
t.left(120)
t.forward(120)

t.left(30) #이어서 그리기 위한 회전

#1.2 (2)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)
t.left(90)
t.forward(120)

turtle.penup()
t.right(30) #이어서 그리기 위한 회전
t.forward(100)
turtle.pendown()

#1.2 (3)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)

turtle.penup()
t.left(30) # 이어서 그리기 위한 회전
t.forward(200) # 가시성을 위해 일부 떨어짐
turtle.pendown()

#1.2 (4)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)
t.forward(50)
t.left(36)


turtle.exitonclick() # turtle 종료