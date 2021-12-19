# 한 자리 숫자가 될 때까지 각 자리 수를 더해줘서 마지막에 3으로 나누어 떨어지면 YES 아니면 NO
# 과정을 몇 번 거쳤는지 카운트 후 출력
# 빠른 입출력을 사용해봤지만 오히려 더 느려짐
# 풀이2 : n = str(sum(map(int, n))) 라는 방식을 적용했던 방식
# 다른 사람의 훨씬 빠른 풀이를 찾아본 결과 알아낸 방법임
# for문 없이 리스트 내부 요소를 바로 더할 수 있음
# 약 1.7배 빠르고 더 짧음
from sys import stdin
input = stdin.readline().rstrip
n = input()
count = 0
while len(n) > 1:
    n = str(sum(map(int, n)))
    count += 1
print("{} \n{}".format(count, "YES" if int(n) % 3 == 0 else "NO"))


# 처음 풀었던 방식, 정답이지만 두 배 정도 느리고 더 길었음
"""
flag, count = 0, 0
while True:
    l = len(n)
    if l == 1 and int(n) % 3 == 0:
        flag = 1
    if l <= 1:
        break
    tmp = 0
    for i in n:
        tmp += int(i)
    n = str(tmp)
    count += 1
print("{} \n{}".format(count, "YES" if flag == 1 else "NO"))
"""