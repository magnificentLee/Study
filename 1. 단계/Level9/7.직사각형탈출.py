# 한수의 위치 x, y
# 왼쪽 아래 = 원점(0, 0)
# 오른쪽 위 꼭짓점 w, h
# 입력 6 2 10 3 출력 1
# 첫 풀이
"""
x, y, w, h = map(int, input().split())
result = [x, y, w - x, h - y]
print(min(result))
"""
# 두 번째
x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))