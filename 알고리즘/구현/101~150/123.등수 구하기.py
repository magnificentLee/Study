# n == p 일 때가 문제일것임 이 때가 등수에 들어올 수 있냐 없냐가 갈리기 때문에
# n == p 이고 가장 끝값과 같거나 보다 작으면 -1이 나오면 될 것
# 전체 랭크 리스트를 만들어 비교하는 방식은 숫자범위가 크기 때문에 안 될 것임
n, s, p = map(int, input().split())  # 랭킹 리스트 숫자, 점수, 랭킹제한
count = 1
if n > 0:
    array = list(map(int, input().split()))  # 내림차순으로 주어짐
    if n == p and array[-1] >= s:
        count = -1
    else:
        for i in range(n):
            if array[i] > s:
                count += 1
            if array[i] == s:
                break
    print(count)
else:
    print(1)

# 처음 사용하려던 방법
# 랭크 리스트를 만들어준뒤 비교하려했지만
# 수의 범위가 넓기 때문에 포기
"""
숫자 이동
n = 10
array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 7]  # 7 추가된 수
for i in range(n, 0, -1):
    if array[i] > array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]
print(array)
"""