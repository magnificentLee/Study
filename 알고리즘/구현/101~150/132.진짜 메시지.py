# 3중 for문으로 각각의 케이스에서 각각의 문자열까지를 검사하려 했으나 100개이하의 테스트 케이스, 10만자 이하의 문자열인 것을 보고
# 시간초과가 발생할 것 같아 다른 방법을 찾는중
# 1중 for문의 솔루션이 732ms 걸리는 것으로 보아 무조건 초과임
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    array = sys.stdin.readline().rstrip()
    l = len(array)
    idx = 0
    alp = [0 for _ in range(26)]
    result = "OK"
    for i in range(l):
        i = i + idx
        if i >= l:
            break
        j = ord(array[i]) - ord("A")
        alp[j] += 1
        if alp[j] == 3:
            if i == l - 1 or array[i] != array[i + 1]:
                result = "FAKE"
                break
            else:
                alp[j] = 0
                idx += 1
    print(result)


# 시간 초과가 발생한 코드
"""
n = int(input())
array = [input() for _ in range(n)]

for i in range(n):
    flag = 1
    l = len(array[i])
    for j in range(l - 1):
        target = array[i][j]
        if array[i].count(target) == 3:
            if j == l - 1 or target != array[i][j + 1]:
                flag = 0
                break
    if flag == 1:
        print("OK")
    else:
        print("FAKE")
"""
