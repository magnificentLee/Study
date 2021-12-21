# 백준 1205 등수 구하기
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