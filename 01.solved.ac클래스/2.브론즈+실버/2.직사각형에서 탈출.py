# 오른쪽 위 꼭짓점이므로 x, y 보다 값이 클 것
# 따라서 w - x, h - y 는 양의 정수가 될 것
# x, y - 원점해봤자 x, y 임
x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))