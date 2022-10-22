import sys
a = int(sys.stdin.readline())
b = []
for i in range(len(str(a))):
    b.append(int(str(a)[i]))
b.sort(reverse = True)
for i in b:
    print(i,end = "")
