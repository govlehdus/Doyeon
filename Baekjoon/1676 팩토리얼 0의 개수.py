import sys
a = int(sys.stdin.readline())
count = 0
for i in range(1,a):
    a *= i
for i in range(1,len(str(a))):
    if str(a)[-i] == "0":
        count += 1
    else:
        break
print(count)
