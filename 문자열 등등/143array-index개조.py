lang = input()
alpha = list("abcdefghijklmnopqrstuvwxyz")
array = [0 for i in range(len(alpha))]

for i in range(len(lang)):
    if array[alpha.index(lang[i])] >= 0:  # 문자가 중복될 경우 포함
        array[alpha.index(lang[i])] += 1
for j in array:
    print(j, end=" ")