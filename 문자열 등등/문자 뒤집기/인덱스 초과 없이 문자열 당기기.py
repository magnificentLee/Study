# 여기까지 문자열을 처음으로 당기는 방법
# 처음 문자열을 뒤에 추가하고 추가한 문자열을 제거
n, m = map(int, input().split())
array = [input() for _ in range(n)]
for i in range(n):
    array.append(array[0])
    del array[0]
    print(array)