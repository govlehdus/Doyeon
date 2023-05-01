a = input()
lst = []
for i in range(len(a)):
    lst.append(a[i:len(a)])
lst.sort()
print("\n".join(lst))
