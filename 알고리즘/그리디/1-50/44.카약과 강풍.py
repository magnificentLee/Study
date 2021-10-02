# 처음 생각한 방법
"""
n, s, r = map(int, input().split())
cayak_no = list(map(int, input().split()))
cayak_ext = list(map(int, input().split()))
count = s

for i in range(s):
    for j in range(r):
        if cayak_no[i] == cayak_ext[j] or abs(cayak_no[i] - cayak_ext[j]) == 1:
            count -= 1
            del cayak_ext[j]
            r -= 1
            break
print(count)
"""
n, s, r = map(int, input().split())
cayak_full = [1] * n
cayak_no = map(int, input().split())
for i in cayak_no:
    cayak_full[i - 1] = 0
cayak_ext = map(int, input().split())
for i in cayak_ext:
    cayak_full[i - 1] += 1
for i in range(n):
    if cayak_full[i] == 0:
        if i == 0:  # 첫 번째 원소일 때
            if cayak_full[i + 1] == 2:
                cayak_full[i + 1] = 1
                cayak_full[i] = 1
        elif i == n - 1:  # 마지막 원소일 때
            if cayak_full[i - 1] == 2:
                cayak_full[i - 1] = 1
                cayak_full[i] = 1
        else:  # 중간 원소일 때
            if cayak_full[i - 1] == 2:
                cayak_full[i - 1] = 1
                cayak_full[i] = 1
                continue
            if cayak_full[i + 1] == 2:
                cayak_full[i + 1] = 1
                cayak_full[i] = 1
                continue
    else:
        continue
print(cayak_full.count(0))