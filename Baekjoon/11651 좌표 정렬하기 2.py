import sys
a = int(sys.stdin.readline())
b= []
for i in range(a):
    b.append(list(map(int,sys.stdin.readline().split())))
b = sorted(b, key = lambda x: (x[1], x[0]))
for i in range(len(b)):
    print(*b[i],sep=" ")
