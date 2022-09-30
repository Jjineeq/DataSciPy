import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("도형그리기", "몇각형을 원하시나요?:")
n = int(s)
l = turtle.textinput("도형그리기", "길이를 몇으로 설정할까요?:")
k = int(l)

for i in range(n):
    t.forward(k)
    t.left(360 / n)
turtle.done()