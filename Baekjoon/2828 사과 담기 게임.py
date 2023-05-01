a = input()
a = a.split(" ")
size = int(a[1])
b = int(input())
lst = []
while b>0:
    c = int(input())
    lst.append(c)
    b -= 1

left = 1
right = size
count = 0

for i in lst:
    if left <= i and i <= right:
        pass
    if left > i:
        num = abs(left - i)
        left -= num
        right -= num
        count += num
    if right < i:
        num = abs(right - i)
        left += num
        right += num
        count += num

print(count)
