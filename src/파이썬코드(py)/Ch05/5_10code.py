import random

tries = 0
guess = 0
answer = random.randint(1, 100)
print("1���� 100 ������ ���ڸ� ���߽ÿ�")
while guess != answer:
    guess = int(input("���ڸ� �Է��Ͻÿ�: "))
    tries = tries + 1
    if guess < answer:
        print("����!")
    elif guess > answer:
        print("����!")
    elif tries == 10:
        print("10�� �õ��߽��ϴ�.")
        break

print("�����մϴ�. �� �õ�Ƚ��=", tries)