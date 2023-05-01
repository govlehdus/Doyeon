import sys
n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()
    for i in command:
        print(i[::-1], end = " ")
