import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup() 
t.goto(100, 100)  
t.write("�� �� ��� ���.")
t.goto(-100, 100)
t.write("ù��° ���� ����.")
t.goto(-100, -100)
t.write("�� �� ��� ����.")
t.goto(100, -100)
t.write("�ι�° ���� ����")

t.goto(0,0)
t.pendown()

a1 = turtle.textinput("", "ù��° ���ڸ� �Է��Ͻÿ�: ")
a2 = turtle.textinput("", "�ι�° ���ڸ� �Է��Ͻÿ�: ")

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