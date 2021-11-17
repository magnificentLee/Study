# 처음
# 1 은 그대로, 2, 3 은 각각의 함수를 만들어 좌우, 상하 반전해서 출력시키는 방식
# 찾아보니 더 간단한 방법도 있음
# 1 = 그대로, 2 = 좌/우, 3 = 상/하
# 깔끔하지 못하기 때문에 수정할 예정
l = int(input())
array = [list(input()) for _ in range(l)]
n = int(input())
if n == 1:
    for i in array:
        print(*i, sep="")
elif n == 2:
    for i in range(l):
        for j in range(l - 1, -1, -1):
            print(array[i][j], end="")
        print()
else:
    for i in range(l - 1, -1, -1):
        for j in range(l):
            print(array[i][j], end="")
        print()