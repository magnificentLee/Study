# 입력 범위가 엄청나게 넓은 문제임 (-2^62 <= array[i] <= 2^62)
# 특정 범위의 리스트를 만들어 사용하면(0~n까지) 원소 하나당 최소 4바이트(실제로는 훨씬 큼)이므로
# 약 32 제타바이트(34억 기가바이트)라는 천문학적인 메모리를 요구함
# 딕셔너리는 삽입한 원소들의 수만큼 메모리를 할당하므로 딕셔너리를 사용하거나 다른 방법을 이용해야할것
# 시간초과로 오답
# reverse 문을 바꿔줬음에도 시간초과 발생
# 결과 리스트로 푸는것 자체가 문제가 있는것 같음
from sys import stdin
input = stdin.readline
n = int(input())
result = {}
for i in range(n):
    tmp = int(input())
    if tmp in result:
        result[tmp] += 1
    else:
        result[tmp] = 1  # 에러 방지
result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
# items = key, value의 쌍을 튜플로 묶은것, x[0] : key값(인덱스), x[1] : value값
print(result[0][0])  # 에러 무시
