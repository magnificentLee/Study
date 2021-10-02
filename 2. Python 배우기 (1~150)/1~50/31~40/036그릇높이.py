n = list(input())
high = 10

for i in range(1, len(n)):  # n[0]은 높이를 일괄적으로 10으로 여기기 때문
    if n[i - 1] != n[i]:
        high += 10
    else:
        high += 5
print(high)


# ((((()() = 60 but 결과는 80
# (((( = 10 + 5 * 3 = 25
# ()() = 10 + 10 * 3 = 40
# 첫 번째는 높이로 10으로 여김
