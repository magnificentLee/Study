# rev() : 역순, rev(rev(x) + rev(y)) 구하기
# x = 123, rev(x) = 321
# y = 100, rev(y) = 001 = 1
# 123 100 = 223  (321 + 1 = 322) = 223
a, b = input().split()
a = a[::-1]
b = b[::-1]
total1 = int(a) + int(b)
total2 = str(total1)[::-1]
print(int(total2))