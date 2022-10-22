a = input()
b = 0
c = 0
ans = 0
lst = []
if "-" not in a:
    a = (a.split("+"))
    for i in a:
        ans += int(i)
else:
    a = a.split("-")
    for i in a:
        if "+" in i:
            i = i.split("+")
            b = 0
            for j in i:
                b += int(j)
            lst.append(b)
        else:
            lst.append(int(i))
    for i in lst:
        ans -= i
    ans += lst[0]*2
                
print(ans)
