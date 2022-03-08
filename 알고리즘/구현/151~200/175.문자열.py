# 순서 중요
# 길이 : a <= b, 소문자로만 구성
# 길이가 같으면서 차이를 최소화 해야함
# adaabc aababbc
# b의 길이가 더 길거나 같기 때문에 b의 인덱스를 늘려가면서 비교
# i, j의 2중 for문에서 a[j], b[i + j]를 비교
a, b = input().split()
n, m = len(a), len(b)
count = m  # 어차피 길이는 b가 더 길기 때문에(같을 수도 있음)
for i in range(m - n + 1):  # 길이가 동일한 경우에도 반복문 작동을 위해 +1
    tmp = 0
    for j in range(n):
        print(a[j], b[i + j])
        if a[j] != b[i + j]:
            tmp += 1
    if tmp < count:
        count = tmp
    print()
print(count)