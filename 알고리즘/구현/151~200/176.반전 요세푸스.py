# 방향 전환을 어떻게 해야되나 고민했던 문제
# 블로그를 찾은 결과 flag = not flag를 이용해 True를 False로, False를 True로 바꾸면 된다는 것을 알게됨
from sys import stdin
input = stdin.readline

n, k, m = map(int, input().split())
array = [i + 1 for i in range(n)]
idx = 0
count = 0
flag = False
while n > 0:
    if count % m == 0:  # 처음엔 n % m으로 했지만 정답이 나오지 않아 count값을 더해가는 방식으로 대조하게끔 변경
        flag = not flag
    if flag:
        idx = (idx + (k - 1)) % n
    else:
        idx = (idx - k) % n
    tmp = array.pop(idx)
    n -= 1
    count += 1
    print(tmp)