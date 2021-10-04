# 내가 생각한 방법 : 리스트 정렬 후 중앙값을 찾아 출력
# math 모듈을 이용해 중앙값을 찾으면 집이 없는 위치를 찍을 수 있기 때문에
# 인덱스를 이용한다

from sys import stdin

input = stdin.readline

n = int(input())
house = sorted(map(int, input().split()))
antenna = house[(n - 1) // 2]
print(antenna)
