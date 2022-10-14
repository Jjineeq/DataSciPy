from operator import length_hint


t = "It's Not The Right Time To Conduct Exams.My DEMAND IN BOLD AND CAPITAL. NO EXAMS IN COVID!!!"

print(t.count("!"))
ch = list(t)
ch1 = length_hint(ch)
ch1 = int(ch1)
Count = 0

for i in range(ch1):
    if ch[i].isupper() == True:
        Count +=1
    else:
        pass

print(Count)