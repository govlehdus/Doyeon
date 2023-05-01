import sys
a = int(sys.stdin.readline())
b = []
for i in range(a):
    b.append(list(map(int,sys.stdin.readline().split())))
b.sort()
for i in range(len(b)):
    print(' '.join(str(x) for x in b[i]))
