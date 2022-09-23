#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 3-2 화씨온도를 섭씨온도로 변환하기, 76쪽
#
#fahrenheit = float(input("화씨온도: "))
#celsius = (fahrenheit - 32.0) * 5.0 / 9.0
#print("섭씨온도:", celsius)

#second = int(input())
global second
second = int(input())
def time(second):
    hour = int(second/3600)
    Min = int(second%3600)
    Second = int(second%3600/60)
    total = "입력한 시간은 {0}시간 {1}분 {2} 초입니다.".foramt(hour, Min, Second)
    print(total)
time(second)
