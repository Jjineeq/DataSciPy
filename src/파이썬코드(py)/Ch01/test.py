num=[[1,2],[3,4],[5,6]]
a=[]

for i in range(3):
    f = num[i]
    for j in range(2):
        a.append(f[j])
print(a)