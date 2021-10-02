from sys import stdin


def octave(n, a, d, array):
    result = 0
    tmp = 0
    for i in range(n):
        if array[i] == a + (tmp * d):
            result += 1
            tmp += 1
    return result


input = stdin.readline

n, a, d = map(int, input().split())
nums = list(map(int, input().split()))
print(octave(n, a, d, nums))