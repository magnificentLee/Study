t = int(input())

for i in range(t):
    lang_list = list(input())
    total = 0
    score = 1
    for i in lang_list:
        if i == "O":
            total += score
            score += 1
        else:
            score = 1
    print(total)