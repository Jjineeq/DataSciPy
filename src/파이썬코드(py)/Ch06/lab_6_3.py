def weeklyPay(rate, hour):
    if (hour > 30):
        money = rate*30 + 1.5*rate*(hour-30)
    else:
        money = rate*hour
    return money

r = int(input("시급을 입력하시오: "))       
h = int(input("근무 시간을  입력하시오: ")) 
print("주급은 " + str(weeklyPay(rate=r, hour=h)))