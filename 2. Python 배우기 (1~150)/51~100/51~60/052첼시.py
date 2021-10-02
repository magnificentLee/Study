# 각 테스트 케이스의 첫 번째 줄 p는 고려해야될 선수의 수이다 (1≤p≤100).
#
# 그 아래 p개의 줄에는 선수의 정보가 표시된다.
#
# 각각의 줄은 선수의 가격 C 와 이름을 입력한다 (C<2*109).
#
# 모든 선수의 가격은 서로 다르다.
# 선수의 이름은 20자 이하여야 하며, 사이에 공백이 있어서는 안 된다.
# 각각의 테스트 케이스에서 가장 비싼 선수의 이름을 출력해야한다.
"""
input
2
3
10 Iversen
1000000 Nannskog
2000000 Ronaldinho
2
1000000 Maradona
999999 Batistuta
output
Ronaldinho
Maradona
"""
n = int(input())

for i in range(n):
    p = int(input())
    max_name = ""
    normal_price = 0
    for j in range(p):
        price, name = input().split()
        price = int(price)
        if price > normal_price:
            max_name = name
            normal_price = price
    print(max_name)