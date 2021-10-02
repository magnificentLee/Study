# A가 받은 표가 B보다 많은 경우에는 A
# B가 받은 표가 A보다 많은 경우에는 B
# 같은 경우에는 Tie
"""
input
6
ABBABB
output
B
"""
t = int(input())
lang_list = list(input())
count_a = count_b = 0
for i in lang_list:
    if i == "A":
        count_a += 1
    else:
        count_b += 1
if count_a > count_b: # 가급적 비교 순서(> = <)에 맞게 작성
    print("A")
elif count_a == count_b:
    print("Tie")
else:
    print("B")
