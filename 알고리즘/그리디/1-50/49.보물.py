# a, b 값을 크기 순으로 정렬하여(a는 역순) 기존 b 인덱스에 맞게끔 배치
# 아래 방법은 정답으로 인정되지만 출제 의도는 아닐것임
"""
n = int(input())
a = sorted(map(int, input().split()), reverse=True)
b = list(map(int, input().split()))
duplicate_b = sorted(b)
result = 0
for i in range(n):
    result += a[i] * duplicate_b[i]
print(result)
"""
# 다음은 내가 푼 방법
n = int(input())
a = sorted(map(int, input().split()), reverse=True)
b = list(map(int, input().split()))
result = 0
for i in range(n):
    result += a[-1] * max(b)
    a.pop()
    b.pop(b.index(max(b)))
print(result)
# 다음은 솔루션 (max(a), min(b)로 해도 맞음)
"""
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for i in range(n):
    result += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
print(result)
"""
