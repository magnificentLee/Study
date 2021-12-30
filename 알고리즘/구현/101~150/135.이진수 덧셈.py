from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    x, y = map(str, input().split())  # 2진수 숫자(0b제외) 입력받기 ex) 1001101 10010
    a, b = int(x, 2), int(y, 2)  # 덧셈을 위해 10진수로 변환하기
    result = bin(a + b)  # 10진수 덧셈후 2진수로 변환(0b포함) ex)0b1011111
    for i in range(2, len(result)):  # 0b를 제외한 2진수만 출력하기
        print(result[i], end="")
    print()

# 처음 풀이 : 정답, 조금 느림
"""
for _ in range(int(input())):
    tmp = input().split()
    a, b = "0b" + tmp[0], "0b" + tmp[1]
    x = int(a, 2)
    y = int(b, 2)
    result = bin(x + y)
    for i in range(2, len(result)):
        print(result[i], end="")
    print()
"""
