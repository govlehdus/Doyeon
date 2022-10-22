import sys
left= list(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
cursor = len(left)
right = []
for i in range(b):
    c = sys.stdin.readline().strip().split()
    if c[0] == "L" and len(left)> 0:
        right.append(left.pop())
    elif c[0] == "D" and len(right)>0:
        left.append(right.pop())
    elif c[0] == "B" and len(left)>0:
        left.pop()
    elif c[0] == "P":
        left.append(c[1])
print("".join(left + list(reversed(right))))
