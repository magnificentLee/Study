# 세 점이 주어질때 직각사각형을 만들기 위한 네 번째 점 출력
# 30 20
# 10 10
# 10 20
# = 30 10
x_list = []
y_list = []
a, b = 0, 0
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
if x_list.count(min(x_list)) > 1:  # 최댓값은 2개만 존재하기 때문
    a = max(x_list)
else:
    a = min(x_list)
if y_list.count(min(y_list)) > 1:  # 최댓값은 2개만 존재하기 때문
    b = max(y_list)
else:
    b = min(y_list)
print(a, b)