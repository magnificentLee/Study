# 반복문을 사용시 시간초과가 발생하므로 수학적으로 해결해야됨
# 매일 올라갔다 미끄러지므로 (a - b) * n
# 꼭대기에 도달시 미끄러지지 않으므로 c - b
# (a - b) * n = c - b => n = (c - b) / (a - b)
# 나머지가 존재할 경우 하루가 더 필요하므로 if문을 사용하거나 올림처리할것
# 1. if문 사용
a, b, c = map(int, input().split())
if (c - b) % (a - b) == 0:
    day = (c - b) // (a - b)
else:
    day = (c - b) // (a - b) + 1
print(day)
"""
# 2. math함수 사용
import math
a, b, c = map(int, input().split())
print(math.ceil((c - b) / (a - b)))
"""