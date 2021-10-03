from sys import stdin
input = stdin.readline

def fix(n, m, array):
    start = array[0]
    end = array[0] + m
    result = 1  # 시작지점도 막아야 되기 때문
    for i in range(n):
        if start <= array[i] < end:
            continue
        start = array[i]
        end = array[i] + m
        result += 1
    return result


n, m = map(int, input().split())
leaks = sorted(map(int, input().split()))
print(fix(n, m, leaks))