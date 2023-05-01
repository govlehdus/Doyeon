a = int(input())
b = []
while a>0:
    c = input()
    c = c.split(" ")
    b.append(c)
    a = a - 1

c = []
d = []


for i in b:
    c.append(int(i[0]))
    d.append(int(i[1]))

if max(c) - min(d) >0:
    print(max(c) - min(d))
else:
    print(0)
