# 요점은 가장 쌀 때 전부 사는것
# 가장 싸지 않다면 다음 도시까지 이동할 만큼만 사서 다음 지역에서 사는것
# minval 값을 최신화 해주면서 result 에 더해주면 되지 않을까?
# 도시의 위치는 변하지 않기 때문에 정렬하면 안 됨!
# 값의 범위가 매우 넓기 때문에 빠른 입력을 해줄것

from sys import stdin as st
n = int(input())  # 도시의 갯수
length = list(map(int, st.readline().split()))
city = list(map(int, st.readline().split()))
minval = city[0]
result = 0
for i in range(n - 1):  # 거리의 수 = 도시의 갯수 - 1
    if city[i] <= minval:
        minval = city[i]
    result += minval * length[i]
print(result)
# len(length)
# n - 1
# 시간차이 없는것으로 결론
