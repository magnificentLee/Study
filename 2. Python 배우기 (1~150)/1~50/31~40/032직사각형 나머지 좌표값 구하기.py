x = []
y = []
new = []  # 정답의 x(new[0]), y(new[1])축
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(1):  # x축 최대/최소 개수 파악
    if x.count(max(x)) < x.count(min(x)):  # 최대값의 개수가 최소보다 적으면
        new.append(max(x))  # 정답의 x는 최댓값
    else:  # 최대가 더 많으면
        new.append(min(x))  # 정답의 x축은 최솟값
for i in range(1):  # y축 최대/최소 개수 파악
    if y.count(max(y)) < y.count(min(y)):  # 최대값이 최소보다 적으면
        new.append(max(y))  # 정답은 최대
    else:  # 최대 > 최소의 경우
        new.append(min(y))  # 정답은 최소
print(new[0], new[1])  # x, y 좌표값

"""
직사각형의 구성요소 = 4개의 점
각각의 점은 x, y축 최소값 4개, 최대값 4개로 구성됨
ex) x,y축 30 20, 10 10, 10 20, 30 10 의 4개의 점은
x축 리스트 : 최소(10) * 2, 최대(30) * 2
y축 리스트 : 최소(10) * 2, 최대(20) * 2 로 구성되어 있다는 뜻
따라서 주어진 3개의 점에서 x축 최대값이 최소값보다 적으면 정답의 x축은 최대일것이고 반대도 성립(최소값)
y축 최대값이 최소값보다 적으면 y축은 최대일 것이고 반대의 경우도 성립(최소값)
input
30 20
10 10
10 20
output
30 10
"""