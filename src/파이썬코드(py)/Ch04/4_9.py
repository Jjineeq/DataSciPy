import random

a = random.randint(1,6)
b = random.randint(1,6)

player1 = input("player1 이름 입력: ")
player2 = input("player2 이름 입력: ")

print(player1)
print(player2)
print("--주사위를 굴립니다.--")
print(player1,"의 주사위 번호는 ", a)
print(player2,"의 주사위 번호는 ", b)
if a>b :
    print(player1,"이 이겼습니다.")
else :
    print(player2,"이 이겼습니다.")

