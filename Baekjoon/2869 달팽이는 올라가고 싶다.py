import math
a,b,c = map(int,input().split())
print(int(math.ceil((c-a)/ (a-b)) +1))
