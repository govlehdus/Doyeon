from collections import Counter
import sys
a = int(sys.stdin.readline())
b = []
for i in range(a):
    b.append(int(sys.stdin.readline()))
b.sort()
c = Counter(b).most_common() 
print(round(sum(b) / len(b)))
print(b[len(b)//2])
if len(c)>1:
     if c[0][1] == c[1][1]:
            print(c[1][0])
     else:
        print(c[0][0])
else:
    print(c[0][0])
print(max(b) - min(b))
