# 일단 기본적인 구조만 구현 하자는 생각으로 풀었다가 통과된 문제임
# 특별히 반례가 있을줄 알았지만 의외로 바로 통과됨
# 아마 다른 언어 기준으로 실버2 문제가 아닌가 생각됨
n = int(input())
array = list(map(int, input().split()))
result = 0
while len(array) > 1:
    a = array.pop(0)
    b = array.pop(0)
    result += a * b
    array.append(a + b)
print(result)