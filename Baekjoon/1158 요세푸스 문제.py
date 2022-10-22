big, small = map(int,input().split())
lst = [i+1 for i in range(big)]
ans = []
count = 0
for i in range(big):
    count += small
    while count > len(lst):
        count -= len(lst)
    ans.append(str(lst.pop(count-1)))
    count -=1
print("<",", ".join(ans),">", sep='')
