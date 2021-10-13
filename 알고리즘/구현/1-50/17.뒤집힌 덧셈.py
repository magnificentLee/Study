# 파이썬의 문자열 다루는법 참고
x, y = input().split()
x, y = x[::-1], y[::-1]
result = int(x) + int(y)
print(int(str(result)[::-1]))