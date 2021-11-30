n, q = map(int, input().split())
array = list(map(int, input().split()))
for _ in range(q):
    tmp = list(map(int, input().split()))
    idx = tmp[0]
    n = tmp[1:]
    result = 0
    if idx == 1:
        for i in range(n[0] - 1, n[1]):
            result += array[i]
        array[n[0] - 1], array[n[1] - 1] = array[n[1] - 1], array[n[0] - 1]
    else:
        front = [n[0], n[2]]
        end = [n[1], n[3]]
        result_tmp = 0
        for i in range(front[0] - 1, end[0]):
            result += array[i]
        for i in range(front[1] - 1, end[1]):
            result_tmp += array[i]
        result -= result_tmp
    print(result)