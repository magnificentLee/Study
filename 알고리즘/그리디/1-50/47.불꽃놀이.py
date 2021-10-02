# 조건 최종 높이 : 시작 < 끝

def fire_crack(n, start, end):
    fire_min = 0
    for i in range(n - 2):
        if i == n - 3:  # 중간에 하나만 남아서 둘 다 터뜨려야 하는 경우
            start -= 1
            end -= 1
        elif start < end:
            end -= 1
        elif start == end:  # 높이가 시작 < 끝이기 때문
            end -= 1
        else:
            start -= 1
    fire_min = max(start, end)
    return fire_min


n = int(input())
fire = list(map(int, input().split()))
start, end = fire[0], fire[-1]
print(fire_crack(n, start, end))
