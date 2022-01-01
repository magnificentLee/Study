# 각 칸을 1씩 잡고 종이 갯수만큼 반복하면서 반복할 때마다 1씩 더해주게?
# m 보다 클 때 카운트해서 결과를 출력하자
# array : 0~99 :100개, 입력좌표 : 100보다 작거나 같은 자연수
# 두 값이 다르기 때문에 인덱스 에러가 발생하는 것 같음
# 따라서 좌표값의 인덱스를 -1씩 해줘야 맞는듯
n, m = map(int, input().split())
array = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y, a, b = map(int, input().split())
    for i in range(x, a + 1):
        for j in range(y, b + 1):
            array[j - 1][i - 1] += 1
result = 0
for i in range(100):
    for j in range(100):
        if array[j][i] > m:
            result += 1
print(result)
