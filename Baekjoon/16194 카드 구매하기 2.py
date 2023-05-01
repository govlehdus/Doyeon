a = int(input())
c = [0] + list(map(int,input().split()))
b = list(c)
for i in range(1,a+1):
    for j in range(0,i):
        if b[i] >  b[i-j]+c[j]:
            b[i] = b[i-j]+b[j]
print(b[a])
