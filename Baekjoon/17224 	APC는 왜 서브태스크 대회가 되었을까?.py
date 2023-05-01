a = list(map(int, input().split()))
lst = []
while a[0] > 0:
    b = list(map(int, input().split()))
    lst.append(b)
    a[0] -= 1
time = a[2]
level = a[1]
score = 0
tri = 0
for i in range(len(lst)):
    if lst[i][1] <= level and tri < time:
        score += 140
        tri += 1
for j in range(len(lst)):
    if lst[j][0] <= level and lst[j][1] > level and tri < time:
        score += 100
        tri += 1

print(score)
