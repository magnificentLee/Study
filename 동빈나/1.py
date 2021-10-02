# 투 포인터
"""
n = [1, 2, 3, 2, 5, 3]  # 현재 방법은 연속 수열이 아닌 띄어도 답이 나올것이므로 틀렸음
count = 0
for i in range(len(n)):
    if n[i] == 5:
        count += 1
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == 5:
            count += 1
print(count)
"""
val = [1, 2, 3, 2, 5]
n, m = len(val), 5  # 리스트 길이, 목표값
result = 0
sum_val = 0  # s
end = 0  # e
for start in range(n):
    while sum_val < m and end < n:
        sum_val += val[end]
        end += 1
    if sum_val == m:
        result += 1
    sum_val -= val[start]
print(result)  # 2 3, 3 2, 5
# s(시작점), e(끝점) 가 있다고 치자
# 합이 5보다 작을 경우 e를 이동시키고 5보다 커진 경우 s를 이동시킨다
# 1     : 작기 때문에 e 이동
# 1 + 2 : 작기 때문에 e 이동
# 1 + 2 + 3 : 크기 때문에(while문 탈출) s 이동(val_sum - val_[start=0]) 1 + 2 + 3 - 1
# 2 + 3 = 5 count + 1
# 2 + 3 + 2 : 크기 때문에 s 이동 // 2 + 3 + 2 - 2
# 3 + 2 = 5 count + 1
# 3 + 2 + 5 > 5 따라서 s 이동 3 + 2 + 5 - 3, 2 + 5 - 2 = 5 count + 1
# 이하 연습
"""
val = [1, 2, 3, 2, 5]
n, m = len(val), 5
result = 0
sum_val = 0
end = 0
for start in range(n):
    while sum_val < m and end < n:
        sum_val += val[end]
        end += 1
    if sum_val == m:
        result += 1
    sum_val -= val[start]
print(result)
"""