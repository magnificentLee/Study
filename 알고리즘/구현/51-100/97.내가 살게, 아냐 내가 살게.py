# 오른쪽으로 진행하면서 중첩되는 방식
# 그 중 K 이상의 값에 가장 먼저 도달하는 행의 시작 인덱스, 도착한 열 인덱스 +1 을 출력하면 될듯
n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
result = [[i + 1, 0, 0] for i in range(n)]
for i in range(m):
    for j in range(n):
        result[j][1] += array[j][i]
        result[j][2] += 1
        if result[j][1] >= k:
            print(result[j][0], result[j][2])
            exit()  # break : 단순 반복문 종료라 예제3번에서 다음 답을 출력하는 오류가 발생함
