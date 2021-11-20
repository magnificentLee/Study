# 1이 등장한 위치부터 0을 카운트해서 더해줌
# 1692ms 의 시간이 걸리는데 보다 더 큰 범위일경우 해당방법은 사용 할 수 없을것임
for _ in range(int(input())):
    m, n = map(int, input().split())
    array = [list(map(str, input().split())) for _ in range(m)]
    result = 0
    for i in range(n):  # 각 행의 동일한 열을 비교해야하기 때문에 arr[0][0], arr[1][0]..
        for j in range(m):
            if array[j][i] == "1":
                for k in range(j, m):  # 리스트의 중간에 1이 나올 경우 다시 이전값들을 더하는문제가 생기기 때문에 j, m 으로 설정
                    result += array[k][i].count("0")
    print(result)
