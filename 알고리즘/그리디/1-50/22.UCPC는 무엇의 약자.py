# Union of Computer Programming Contest club contest
# UCPC가 입력으로 들어와도 love,
# U C C P C C가 입력으로 들어와도 love가 출력되어야 합니다.
n = input()
alpha = ["U", "C", "P", "C"]
temp = 0
for i in alpha:
    if i in n:
       temp += 1
       n = n[n.index(i) + 1:]
    else:
        print("I hate UCPC")
        break
if temp == 4:
    print("I love UCPC")
# 시도1 : 틀림
"""
n = input().split()
result = []
for i in n:
    if i[0].isupper():
        result.append(i[0])
if "".join(result) == "UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")
"""