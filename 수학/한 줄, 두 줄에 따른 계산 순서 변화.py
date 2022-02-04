# 치환을 이용한 피보나치 풀이중 확인했던 것
n = int(input())
a, b = 0, 1
for _ in range(n):
    a = b
    b = a + b
    print(a, b)
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
    print(a, b)
# 같은 코드라도 한 줄로 놓느냐 두 줄로 놓느냐에 따라 결과가 확연히 바뀐다는 것을 알았음
# 위의 경우 a = b의 순서를 바꿔도 결과가 똑같이 2^n 을 구하는 식이 되었고
# 아래의 경우 피보나치를 구하는 식이 되었음 (n=10일 때 a=512, 55)
# 아마 C에서 ++i, i++ 같이 이번 경우에서 바로 적용하느냐 아니면 다음 반복에서 적용하느냐의 차이와 같지 않을까?
