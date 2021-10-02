# 시간초과
"""
from sys import stdin as st

n = int(st.readline())
rice = list(map(int, st.readline().split()))
result = []
# result 라는 리스트에 값을 한 번 더 저장해서 max를 찾는 과정에서 시간 초과가 발생하는 것 같음
# 계수 정렬을 사용하는 건 어떨까?
for i in set(rice):
    result.append(rice.count(i))
print(max(result))
"""
# 시간초과로 인해 계수정렬을 사용한 방법
from sys import stdin as st

n = int(st.readline())
rice = map(int, st.readline().split())
result = [0] * 50001  # 전체 범위 1<= n <= 50000 총 5만개 but 0이 아닌 1부터 시작이므로
# 5만+1
for i in rice:
    result[i] += 1
print(max(result))
""" 깔끔하게 다듬은것
from sys import stdin

input = stdin.readline

n = int(input())
rice = map(int, input().split())
result = [0] * 50001  # 전체 범위 1<= n <= 50000 총 5만개 but 0이 아닌 1부터 시작이므로
# 5만+1
for i in rice:
    result[i] += 1
print(max(result))
"""