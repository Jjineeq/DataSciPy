def fibo():
    k = int(input())
    n = 1
    result1 = 2
    result2 = 3
    for n in range(k):
        if n <= 1:
            print(1+2)
            n = n+1
        else:
            result3 = result1 + result2
            print(result3)
            result1 = result2  
            result2 = result3
            n = n+1
            
fibo()