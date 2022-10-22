import sys
a = int(sys.stdin.readline())
b = []
for i in range(a):
    b.append(sys.stdin.readline().strip())
b = list(set(b))
b.sort()
b.sort(key = len)
for i in b:
    print(i)
