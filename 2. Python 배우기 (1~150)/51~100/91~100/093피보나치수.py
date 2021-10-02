# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 이하 검증값으로 사용가능
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
ini = 0  # initial value 초기값
a = 1
b = 0

for i in range(int(input())):
    b = ini
    ini = a
    a = b + ini

print(ini)