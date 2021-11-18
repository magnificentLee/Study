# 처음 생각했던 방식 : a, b, c를 각각의 새로운 변수에 전부 더하면서 3을 카운트하는 별도의 변수에 저장,
# 점수가 같을 경우 3을 카운트 한 변수 혹은 리스트에서 3이 가장 많은 변수를 출력하는 방식
# 하지만 이것보다 더 편한 방식이 존재 = 애초에 3을 제곱하여 더하는 것, 3을 제곱해서 더하면 각각의 값이
# 제곱하지 않았을 때에 비해 유니크함을 가지게 된다
x, y, z, l, m, n = 0, 0, 0, 0, 0, 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    l += a  # 최댓값 저장용(출력용), 이하 동일
    m += b
    n += c
    x += a**2  # 최댓값 판별용, 이하 동일
    y += b**2
    z += c**2
result = [x, y, z]  # 판별용 최댓값
ini_res = [l, m, n]  # 출력용 최댓값
m = max(result)
idx = result.index(m)
if result.count(m) > 1:  # 복수의 최댓값을 가질 경우
    print(0, ini_res[idx])
else:  # 최댓값이 하나인 경우
    print(idx + 1, ini_res[idx])