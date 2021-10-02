# 최솟값의 조건(미달시 -1 출력하는 조건) (k * (k + 1)) // 2
# 출력 조건 (n - 최솟값) % k == 0 : k - 1 else: k
n, k = map(int, input().split())
min_val = (k * (k + 1)) // 2
if min_val > n:
    print(-1)
elif (n - min_val) % k == 0:
    print(k - 1)
else:
    print(k)