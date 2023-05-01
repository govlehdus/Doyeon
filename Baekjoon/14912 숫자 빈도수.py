a,b = map(int,input().split())
c = ''
for i in range(1,a+1):
    c += str(i)
print(c.count(str(b)))
