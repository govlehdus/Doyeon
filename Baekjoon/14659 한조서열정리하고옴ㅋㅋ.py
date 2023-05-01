a = int(input())
b = input()

b = b.split(" ")
count = 0
word = 0
lst = []
ans = 0
for i in b:
    # 4 6
    if int(i) > int(word):
        word = i
        lst.append(count)
        count = 0
    # 6  4
    else:
        count += 1
    ans = max(ans, count)
print(ans)
