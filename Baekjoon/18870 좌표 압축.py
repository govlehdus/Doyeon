n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))
dic1 = {arr2[i]:i for i in range(len(arr2))}
for i in arr:
    print(dic1[i], end = ' ')
