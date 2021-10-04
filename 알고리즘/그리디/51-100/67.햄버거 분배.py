# H 버거위치 P 사람위치

from sys import stdin

input = stdin.readline


def share(n, k, array):
    result = 0
    for i in range(n):
        if array[i] == "P":
            # 만약 i + k 로 하면 k = 1, i = 2 일때 i-1=1, i+k=3이지만 for문으로 돌리면 1~2까지이기 때문
            for j in range(i - k, i + (k + 1)):
                if 0 <= j < n and array[j] == "H":  # 인덱스 범위내에서, 값이 햄버거라면
                    result += 1
                    array[j] = "N"  # 중복되지 않게 계산된건 제거
                    break
    return result


n, k = map(int, input().split())
burgers = list(input().rstrip())
print(share(n, k, burgers))

