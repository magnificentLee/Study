# 문제를 잘못이해하면 안 된다, 조건을 제대로 볼 것
# "제일 작은 종말의 숫자는 666이고" 즉, N 번째로 작은 666을 가진 숫자를 원하는 것
# 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, ...
""" 틀린 방법
n = int(input())
print(str(n - 1) + "666")
"""
n = int(input())
count = 0
movie_name = 666
while True:
    if "666" in str(movie_name):
        count += 1
        if count == n:
            print(movie_name)
            break
    movie_name += 1