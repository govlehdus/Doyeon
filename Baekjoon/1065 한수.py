a = int(input())
b = [True] * (a+1)
count = 0

if a >=100:
    for i in range(1,100):
        b[i] = False
    for i in range(100, a+1):
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            b[i] = False
    for i in range(len(b)):
        if b[i] == False:
            count += 1
    print(count)
else:
    print(a)
