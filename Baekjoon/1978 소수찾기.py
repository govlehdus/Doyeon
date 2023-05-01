a = int(input())
b = list(map(int,input().split()))
if 1 in b:
    b.remove(1)
count = 0
for i in b:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count +=1
        
        
print(count)
