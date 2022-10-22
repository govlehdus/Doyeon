a = int(input())
b = []
c = []
d = 1
e = True
for i in range(a):
    f = int(input())
    while d <=f:
        c.append(d)
        b.append("+")
        d += 1
    if c[-1] == f:
        c.pop()
        b.append("-")
    else:
        e = False
if e == False:
    print("NO")
else:
    print("\n".join(b))
