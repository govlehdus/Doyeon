#import sys
n = int(input())

for i in range(n):
    command = input()
    ret = ""
    count = 0
    for i in range(len(command)):
        if command[i] == "(":
            count +=1
        else:
            count -=1
        if count == -1:
            ret = "NO"
    if ret == "NO":
        print("NO")
    elif count == 0 :
        print("YES")
    else:
        print("NO")
