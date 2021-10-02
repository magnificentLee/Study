# 아스키코드를 이용하는 방법
"""
alpha = list(range(65, 91))  # 아스키코드 A~Z
n = input()
n_list = []
total = 0
for i in n:
    n_list.append(ord(i))
for i in n_list:
    if i in [65, 66, 67]:
        total += 3
    elif i in [68, 69, 70]:
        total += 4
    elif i in [71, 72, 73]:
        total += 5
    elif i in [74, 75, 76]:
        total += 6
    elif i in [77, 78, 79]:
        total += 7
    elif i in [80, 81, 82, 83]:
        total += 8
    elif i in [84, 85, 86]:
        total += 9
    elif i in [87, 88, 89, 90]:
        total += 10
print(total)
"""
# 알파벳 리스트를 이용
alpha = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
n = input()
total = 0
for i in alpha:
    for j in range(len(n)):
        if n[j] in i:
            total += alpha.index(i) + 3
print(total)