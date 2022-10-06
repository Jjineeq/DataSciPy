import random

cal=[]
cal.append("1+2")
cal.append("3+4")
cal.append("4+5")
cal.append("5+6")
cal.append("6+7")
cal.append("7+8")
cal.append("8+9")
cal.append("9+10")
cal.append("10+11")
cal.append("11+12")
cal.append("12+13")

a = random.choice(cal)
print(a,"=",eval(a))