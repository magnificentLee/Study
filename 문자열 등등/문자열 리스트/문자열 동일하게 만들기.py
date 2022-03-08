# 백준 1120 문자열
# 두 문자열을 비교할 때 동일하게 만들기 위해 문자를 추가한다고 하자
# 이 때 추가할 문자의 최소 갯수를 구하기
# 순서 중요
# 길이 : a <= b, 소문자로만 구성
# adaabc aababbc
a, b = input().split()
n, m = len(a), len(b)
count = m  # 어차피 길이는 b가 더 길기 때문에(같을 수도 있음)
for i in range(m - n + 1):  # 길이가 동일한 경우에도 반복문 작동을 위해 +1
    tmp = 0
    for j in range(n):
        if a[j] != b[i + j]:
            tmp += 1
    if tmp < count:
        count = tmp
print(count)
