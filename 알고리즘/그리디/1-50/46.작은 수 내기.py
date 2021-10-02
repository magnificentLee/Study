n = int(input())

joo = sorted(map(int, input().split()), reverse=True)
boss = sorted(map(int, input().split()))
result = 0
for i in range(n):
    if joo[i] >= boss[-1]:
        pass
    else:
        result += 1
        boss.pop()
if result >= (n + 1) // 2:
    print("YES")
else:
    print("NO")

# 첫 시도 : 해당 바리에이션들은 전부 16퍼센트에서 실패함(틀렸거나 출력초과)
"""
n = int(input())

joo = sorted(map(int, input().split()))
boss = sorted(map(int, input().split()))
start = 0
result = 0
for i in range(n):
    for j in range(start, n):
        if joo[i] < boss[j]:
            result += 1
            start = j
    if result > (n + 1) // 2:
        print("YES")
        break
else:
    print("NO")
"""