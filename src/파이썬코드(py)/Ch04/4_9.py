import random

a = random.randint(1,6)
b = random.randint(1,6)

player1 = input("player1 �̸� �Է�: ")
player2 = input("player2 �̸� �Է�: ")

print(player1)
print(player2)
print("--�ֻ����� �����ϴ�.--")
print(player1,"�� �ֻ��� ��ȣ�� ", a)
print(player2,"�� �ֻ��� ��ȣ�� ", b)
if a>b :
    print(player1,"�� �̰���ϴ�.")
else :
    print(player2,"�� �̰���ϴ�.")

