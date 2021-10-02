string = input()
alp = ["U", "C", "P", "C"]
tmp = 0
for i in alp:
    if i in string:
        tmp += 1
        string = string[string.index(i) + 1:]
    else:
        print("I hate UCPC")
        break
if tmp == 4:
    print("I love UCPC")