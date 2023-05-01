rope = int(input())
#while True:
lst = []
while rope > 0:
    a = int(input())
    lst.append(a)
    rope -= 1
lst.sort(reverse = True)
ls = []
a = 1
for i in lst:
    ls.append(i*a)
    a+=1
print(max(ls))
