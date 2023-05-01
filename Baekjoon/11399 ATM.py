a = input()
b = list(map(int, input().split()))
b = sorted(b)
ti = 0
time = 0
for i in b:
    ti += i
    time += ti
print(time)
