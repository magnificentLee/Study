# 집합과 리스트의 차이가 보이는 문제
# 중복 제거는 어떻게 할까 -> 리스트? : 순서가 다르면 거짓이나옴
# 집합을 사용한 결과 순서가 달라도 정답이 나옴  => 집합을 사용
array = set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:  # ex) 1:3, 1:4
        tmp = 10 * a + b
    else:
        tmp = 10 * b + a
    array.add(tmp)
if array == {13, 14, 34}:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")

# 아래와 같이 집합은 순서가 달라도 요소가 같으면 True 가 나오지만
# 리스트는 요소가 같아도 순서가 다르면 False가 나온다
"""
a = set()
b = {13, 14, 44}
a.add(13)
a.add(44)
a.add(14)  # a = {13, 44, 14}
print(a == b)
c = [1, 2, 3, 4]
d = [4, 3, 1, 2]
print(c == d)
"""