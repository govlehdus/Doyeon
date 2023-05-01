a = int(input())
b = [0,1,2] + [10007] * (a)
for i in range(3,a+1):
    b[i] = b[i-2] + b[i-1]
print(b[a]%10007)
