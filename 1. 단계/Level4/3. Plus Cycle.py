# // : 몫 , % : 나머지
""" 10으로 나눴을 떄
26(초기값) = 2(몫)+6(나머지) = 0(몫)8(나머지) -> 6(나머지)8(나머지) = 6(몫)+8(나머지) = 14
84 = 8(몫)+4(나머지) = 12 -> 42 = 4+2 = 6 -> 26(최종값)
초기값 = 몫1 + 나머지1 = 총합(몫2/나머지2) -> 나머지1나머지2 ...
"""
import sys

a = b = int(sys.stdin.readline())
count = 0
while True:
    ten = a // 10
    one = a % 10
    total = ten + one
    count += 1
    a = int(str(one) + str(total % 10))
    if a == b:
        break
print(count)
