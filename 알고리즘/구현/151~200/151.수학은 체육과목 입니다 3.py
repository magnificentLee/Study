# 시작 지점을 특정하는 방법이 중요하다.
#
# 시작 지점을 임의의 수로 생각하는게 아니라, 특정 길이의 수로 보고 탐색하면
# 빠르고, 간단하게 처리할 수 있다
s = input()
l = len(s)
for i in range(l):
    target = s[:i + 1]
    n = int(target)

    while True:
        if len(target) >= l:
            break
        n += 1
        target += str(n)

    if target == s:
        print(s[:i + 1], n)
        break
"""
s = input()
for start_len in range(1, len(s) + 1):
    s2 = s[:start_len]
    n = int(s2)

    while len(s2) < len(s):
        n += 1
        s2 += str(n)

    if s2 == s:
        print(s[:start_len], n)
        break
"""