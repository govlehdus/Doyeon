a = [True] * 10000
a[0] = 1
for i in range(10000):
    c = i
    for j in range(len(str(i))):
        c += int((str(i))[j])
    if c < 10000:
        a[c] = False
    else:
        pass
for i in range(len(a)):
    if a[i] == True:
        print(i)
