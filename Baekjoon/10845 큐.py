import sys
a = int(sys.stdin.readline())
lst = []
for i in range(a):
    c = sys.stdin.readline().split()
    if c[0] =="push":
        lst.append(c[1])
    elif c[0] == "pop":
        if lst:
            print(lst.pop(0))
        else:
            print(-1)
    elif c[0] == "size":
        print(len(lst))
    elif c[0] == "empty":
        if lst:
            print(0)
        else:
            print(1)
    elif c[0] == "front":
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif c[0] == "back":
        if lst:
            print(lst[-1])
        else:
              print(-1)
