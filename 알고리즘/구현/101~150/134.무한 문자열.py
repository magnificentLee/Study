# 길이로 나누어 떨어지면서 동일한 문자열일때?
# 각각의 인덱스를 비교하되 길이가 달라 인덱스를 초과하는 경우는?
# abc    : idx 0 1 2 0 1 2 0 1 2 0 1 2
# abcabc : idx 0 1 2 3 4 5 0 1 2 3 4 5
# 최대 길이만큼 반복하되 짧은 쪽의 문자열의 길이를 나눈 나머지가 인덱스값인듯
# 최대 길이만큼 반복 -> 오답
# 두 값의 길이를 곱한 만큼 반복
s = input()
t = input()
s_len, t_len = len(s), len(t)
m = s_len * t_len # max of length
flag = 1
for i in range(m):
    if s[i % s_len] != t[i % t_len]:
        flag = 0
        break  # 시간 절약
print(flag)