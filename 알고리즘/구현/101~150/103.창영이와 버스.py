# 문제를 이해하는데 시간이 꽤 걸렸음(마지막 요금 부분 때문에)
# 행 인덱스: 출발지, 열 인덱스: 도착지(요금), 1,1 / 2,2.. 출발 도착지가 같은 경우는 없으니 대각선으로 비어있는것
# 버스 번호 3 1 2 가 각각이 행,열이 된다고 생각하면 반복문으로m-1 만큼 반복하면서
# 행 = 인덱스[i] - 1, 열= 인덱스[i+1]-1
# 다만 열을 이렇게 하면 1 2 0 4 가 아닌 0 4 1 2 가 주어질 경우 도착지가 1이 아닌 0으로 설정되지 않을까?
# -> 문제를 잘못 이해했던것, 각각의 열은 모두 도착지 및 요금임 모두 정렬된 상태로 주어진다는 뜻임

n, m = map(int, input().split())
bus = list(map(int, input().split()))
charge = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(m - 1):
    result += charge[bus[i] - 1][bus[i + 1] - 1]
print(result)