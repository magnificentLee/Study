# 제일 위, 0,0 시작점에서 공을 떨어트렸을때 얼마나 갈 수 있는지 물어보는 문제
# 예제1의 경우 Lorem, o, ., o. 총 8
# 예제2의 경우 S~!
# 공백 기준으로 끊지 않고, n[i] 가 공백일때 정지하게?
# 공백까지의 거리를 측정, 다음 문장은 이 거리부터 시작
while True:
    n = int(input())
    if n == 0:
        break
    tmp = 0
    result = 0
    for _ in range(n):
        string = input()
        for i in string[tmp:]:
            if i == " ":
                break
            tmp += 1
    result += tmp + 1
    print(result)
"""
abcde : 5
abcdef: 6
abcdefg:7
하지만 tmp는 인덱스 값을 기준으로 계산되기 때문에 마지막에 +1을 해줘야 맞을것
"""
