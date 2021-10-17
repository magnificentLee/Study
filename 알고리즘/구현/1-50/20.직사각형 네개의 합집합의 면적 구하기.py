# 처음 생각 -> 좌표의 범위만큼 반복문을 돌려준 다음 중복되는 값을 제거
# 생각보다 구현이 힘들었기 때문에 다른 코드들을 참고함
# - - - - - - - - -
# 전체 크기는 정해져 있기 때문에 전체 크기 만큼의 범위 리스트를 만들어준뒤
# 입력된 좌표만큼 반복문 실행, 해당되는 좌표값을 1로 만들어준다
array = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x, y, x1, y1 = map(int, input().split())
    for i in range(x, x1):
        for j in range(y, y1):
            array[i][j] = 1
result = 0
for i in array:  # 2중 리스트이기 때문에 sum(array)는 에러가 발생함
    result += sum(i)
print(result)