import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("�����׸���", "����� ���Ͻó���?:")
n = int(s)
l = turtle.textinput("�����׸���", "���̸� ������ �����ұ��?:")
k = int(l)

for i in range(n):
    t.forward(k)
    t.left(360 / n)
turtle.done()