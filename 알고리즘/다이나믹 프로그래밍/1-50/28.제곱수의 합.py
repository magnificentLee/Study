# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 1 2 3 1 2 3 4 2 1 2   3  4  2
# 내가 생각한건 다 맞았는데 마지막 하나를 놓쳐서 시간이 오래걸림
# i ** i 가 아니라 i * i 즉, i ** 2였음

n = int(input())
array = [i ** 2 for i in range(1, 317)]
dp = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = []
    for j in array:
        if j > i:
            break
        tmp.append(dp[i - j])
        print(i, j, tmp)  # 작동과정 확인용
        # print(tmp)
    dp[i] = min(tmp) + 1
print(dp[n])


"""
n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = i
    for j in range(1, i):
        if j ** 2 > i:  # n = 9 일 때, 4 ** 2 = 16으로 n을 초과하는 경우
            break
        if dp[i] > dp[i - j ** 2] + 1:
            dp[i] = dp[i - j ** 2] + 1
print(dp[n])
"""
# 빠른 입력과 제곱근까지로 범위를 낮춘 경우
# 이해가 안 되는건 오히려 시간이 더 걸렸다는 점임
# 기존은 4412ms, 새로운건 4620ms 서버상태를 고려하면 차이가 없거나 오히려 더 느렸다는 건데 왜 그런거지?
"""
import sys

n = int(sys.stdin.readline())
array = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]  # 제곱근
dp = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = []
    for j in array:
        if j > i:
            break
        tmp.append(dp[i - j])
    dp[i] = min(tmp) + 1
print(dp[n])

"""