a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
b = input()
count = 0
for i in (a):
    if i in b:
        b = b.replace(i,'a')
count += len(b)
print(count)
