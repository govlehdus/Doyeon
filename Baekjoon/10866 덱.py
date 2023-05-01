import sys
from collections import deque
a = int(sys.stdin.readline())
lst = deque()
for i in range(a):
    b = sys.stdin.readline().split()
    if b[0] =="push_back":
        lst.append(b[1])
    elif b[0] =="push_front":
        lst.appendleft(b[1])
    elif b[0] =="pop_back":
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif b[0] =="pop_front":
        if lst:
            print(lst.popleft())
        else:
            print(-1)
    elif b[0] =="size":
        print(len(lst))
    elif b[0] =="empty":
        if lst: print(0)
        else: print(1)
    elif b[0] =="front":
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif b[0] =="back":
        if lst:
            print(lst[-1])
        else:
            print(-1)
