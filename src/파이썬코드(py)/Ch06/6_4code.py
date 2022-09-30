def fibonacci(n):
    fibList = [1,1]
    if n == 1 or n == 2:
    	return 1
    for i in range(2, n):
    	fibList.append(fiblist[i-1] + fibList[i-2])
        return fibList
        

i = int(input("숫자입력: "))
print(fibonacci(i))