count = 0
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    count += 1
    result = ""
    while True:
        if n % 2 == 0:  # n이 짝수이면
            n //= 2
            tmp = True  # 짝수 판별 코드
        else:  # n이 홀수이면
            n = n // 2 + 1
            tmp = False
        if n < 2:
            break
        for i in range(n):
            if tmp is False and i == n - 1:
                array[i] *= 2
            else:
                array[i] += array[-1]
                del array[-1]
    if array[0] > array[1]:
        result = "Alice"
    else:
        result = "Bob"
    print("Case #{}: {}".format(count, result))

# 처음 풀었던 오답, 초기에 짝수가 주어질때 제대로 작동하지 않음
# 시행 착오 결과 짝수 판별 코드를 넣어주는 것으로 해결함
# 인덱스에러
"""
case = 0
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    idx = 0
    case += 1
    while True:
        l = len(array)
        if l == 2:
            break
        if l % 2 != 0:
            array[l // 2] += array[l // 2]
        if l == 3:
            array[0] += array[-1]
        array[idx] += array[-1]
        del array[-1]
        print(array)
        idx += 1
    if array[0] > array[1]:
        result = "Alice"
    elif array[0] < array[1]:
        result = "Bob"
    print("Case #{}: {}".format(case, result))
"""