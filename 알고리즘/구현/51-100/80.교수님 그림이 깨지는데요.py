n, k = map(int, input().split())
bit = [input().split() for _ in range(n)]

for i in range(n):
    for _ in range(k):
        for j in range(n):
            print((bit[i][j] + " ") * k, end="")
        print()

# 코드1 : 출력 결과 각 숫자 사이에 공백이 있는걸 놓쳤음
"""
n, k = map(int, input().split())
bit = [input().split() for _ in range(n)]

for i in range(n):
    for _ in range(k):
        tmp = ""
        for j in range(n):
            tmp += bit[i][j] * k
        print(tmp)
"""