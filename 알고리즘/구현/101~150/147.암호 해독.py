# 97, 122 = a, z
import sys

code = sys.stdin.readline().rstrip()
words = [sys.stdin.readline().rstrip() for _ in range(int(input()))]
for j in range(26):
    result = ""
    for i in code:
        tmp = ((ord(i.upper()) - 97 + j) % 26) + 97
        result += chr(tmp)
    for i in words:
        if i in result:
            print(result)
            exit()
# 기존 정답 문자열 찾는 방식 (오답)
# for j in range(1, 26):
#     result = ""
#     for i in code:
#         tmp = ord(i.lower()) - j  # 17이 얼마인지 모름, 26일때 원본, 그이후로 1~25와 동일하므로 1~25의 값으로 생각하자
#         if tmp < 97:
#             tmp = 123 - (97 - tmp)
#         result += chr(tmp)