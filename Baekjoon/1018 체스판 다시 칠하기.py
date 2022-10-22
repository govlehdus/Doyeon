a,b = map(int,input().split())
c = []
d = []
for i in range(a):
    c.append(input())
for x in range(a-7):
    for z in range(b-7):
        count1 = 0
        count2 = 0
        for i in range(x, x+8):
            for j in range(z,z+8):
                if (j+i)%2 ==0:
                    if c[i][j] != "B" : count1 +=1
                    if c[i][j] != "W" : count2 +=1
                else:
                    if c[i][j] != "W" : count1 +=1
                    if c[i][j] != "B" : count2 +=1
        d.append(count1)
        d.append(count2)
print(min(d))
