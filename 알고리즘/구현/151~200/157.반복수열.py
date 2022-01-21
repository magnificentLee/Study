# 특정값 이후로 계속 반복되는 수열일것임
# 따라서 반복이 시작되는 특정값일 때 반복문을 종료, 특정값 직전(특정값의 인덱스)까지의 거리를 출력하면 될것
# 예를들면 a b c d e f d e f d e f... 이런식이면 a b c = 3이라는뜻
a, p = map(int, input().split())
# 반복 확인용 리스트
result = [a]
while True:
    tmp = 0
    for i in str(result[-1]):
        tmp += int(i) ** p
    if tmp in result:  # 반복되면 종료
        break
    result.append(tmp)
print(result.index(tmp))
