n = int(input())
cups = input()
two = cups.count("LL")
if two <= 1:
    print(len(cups))
else:
    print(len(cups) - two + 1)
# 첫 시도 방식 : 틀림
"""
n = int(input())
cups = input()
a = cups.count("S")
b = cups.count("LL")
print(a + b + 1)
"""
# 1, S를 넣을 경우 2가 나옴
# 컵 홀더에 놓을 수 있는 최대 사람의 수를 구하는 문제
# 한 사람당 하나의 음료를 들고 가기 때문에 솔로석 한명의 경우 1이 나와야함
# 따라서 기존의 방식은 틀림