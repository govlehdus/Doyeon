a = []
for i in range(9):
    a.append(int(input()))
total = sum(a) -100
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == total:
            num1,num2 = a[i],a[j]
            a.remove(num1)
            a.remove(num2)
            break
    if len(a)<9:
        break
a.sort()
for i in range(len(a)):
    print(a[i])
