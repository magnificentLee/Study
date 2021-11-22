# 원래 생각했던 방식 : 리스트를 만들고 기존 리스트를 바탕으로 r*x, c*y 의 새로운 리스트를 만드는것
# 리스트를 두 번 만드는 방식이므로 비효율적임, 이 방식이 정답은 아닐것임
r, c, x, y = map(int, input().split())  # r, c = 기존 행 렬, r*x, c*y = 수정된 행 렬
result = []
for i in range(r):
    scan = input()
    for j in range(x):
        tmp = ""  # 초기값 및 초기화용
        for k in range(c):
            tmp += scan[k] * y
        result.append(tmp)
print(*result, sep="\n")