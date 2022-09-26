check = float(input("여성이면 1, 남성이면 0을 입력하세요: "))
weight = input("몸무게: ")
waist = input("허리둘레: ")
wrfm =76-(28* weight/waist)
mrfm = 64-(20* weight/waist)

if check == 0:
    print(wrfm)
else:
    print(mrfm)

