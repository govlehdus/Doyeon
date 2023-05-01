nums, price = list(map(int, input().split()))
lst = []
count = 0
for i in range(nums):
    lst.append(int(input()))
lst.sort(reverse = True)

for i in range(nums):
    if price == 0:
        break
    if lst[i] > price:
        continue
    count += price // lst[i]
    price %= lst[i]


print(count)

