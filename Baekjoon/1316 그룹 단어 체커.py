a = int(input())
count = 0
for i in range(a):
    b = input()
    c = [""]
    for x in range(len(b)):
        if b[x] == c[-1]:
            pass
        else:
            c.append(b[x])
    d = [" "]
    for j in range(len(c)):
            if c[j] in d[0:-1]:
                count += 1
                break
            else:
                d.append(c[j])    
    
print(a-count)
