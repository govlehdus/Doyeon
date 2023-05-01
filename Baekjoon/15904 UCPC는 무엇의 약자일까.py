sentence = input()
ch = ["U", "C", "P","C"]
check = True

for i in range(len(ch)):
    if ch[i] in sentence:
        check = True
        idx = sentence.find(ch[i])
        sentence = sentence[idx +1:]
    else:
        check = False
        break
if check == True:
    print("I love UCPC")
else:
    print("I hate UCPC")
