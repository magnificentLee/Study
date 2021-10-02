# x, y 카드를 골라 더한다
# 결과값을 x, y에 덮어 쓴다
# 기존 카드 + 새로운 x, y를 더한 값의 최솟값
# input = 3 2 6
# output = 5(3 + 2), 5(2 + 3), 6 = 16
# input = 4 2 3 1
# output = 4 3 3 3, 4 6 6 3 = 19
# 카드의 개수가 2~1000, 각각의 카드의 값이 백만까지 가기 때문에 시간초과를 조심해야함
# 새로운 값을 리스트화 하는 방식은 분명히 시간초과 할 것이기 때문에
# 기존 리스트의 값을 대체하는 방식으로 해보자
from sys import stdin  # 빠른입력
n, m = map(int, stdin.readline().split())
# 어차피 for문에서 정렬하기 때문에 따로 sorted X, 다순 list화
card = list(map(int, stdin.readline().split()))
for i in range(m):  # 아래 과정을 m번 반복
    card.sort()  # 가장 낮은 값 두 개가 필요하기 때문에 오름차순으로 정렬
    result = card[0] + card[1]  # 가장 낮은 값 두 개 = x, y 를 더해서
    card[0] = result  # 각각의 값을 새로운 값으로 대체
    card[1] = result
    # 새로운 값이 나와도 for문에서 sort하기 때문에 값은 계속 오름차순으로 정렬 될 것임
print(sum(card))



# 추가
# 13975(G4), 1715(G4) 와 비슷하다고 하니 찾아볼것
