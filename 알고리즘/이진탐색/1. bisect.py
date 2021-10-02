from bisect import bisect_left, bisect_right
# 정렬된 리스트에서 해야됨
a = [1, 2, 2, 4, 4, 5]
x = 4
# 리스트 왼쪽에서 4의 처음 위치 찾기
print(bisect_left(a, x))
# 리스트 오른쪽에서 4의 처음 위치 찾기
print(bisect_right(a, x))
# 리스트에서 4의 개수 구하기
print(bisect_right(a, x) - bisect_left(a, x))

# 즉, 특정 값의 인덱스 위치를 찾는 것이라 생각하면 됨