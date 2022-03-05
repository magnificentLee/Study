# 백준 6986 절사평균
# float 을 이용하기 때문에 부동소수점 에러가 발생하지 않을까 걱정임 => 시간초과 이후 오답이 출력된건 이것 때문인 것 같음
# 실제 값이 10.105여야 하는데 10.1049999999999로 저장되었을 때 문제가 된다는 것
# 파이썬엔 double 형태가 없기 때문에 float의 오차를 조정해줘야 되는데 어떻게 해야 될까? => 수동 보정(결과에 1e-8을 더해줌)
# 4024ms가 걸림 => 일반적인 방법으로는 절대 못 풀음
n, k = map(int, input().split())
array = sorted([float(input()) for _ in range(n)])
res1 = sum(array[k:n - k]) / (n - 2 * k)
res2 = (sum(array[k: n - k]) + k * (array[k] + array[n - k - 1])) / n
print("%.2f" % (res1 + 1e-8))
print("%.2f" % (res2 + 1e-8))