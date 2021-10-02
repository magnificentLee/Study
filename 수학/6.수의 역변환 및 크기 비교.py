# 외부 도움X
# 과정
# 입력 : 734 893, 출력 : 437
""" 기존
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
"""
""" 1.
a = list(input().split())
a_list = [int(i[::-1]) for i in a]
print(max(a_list))
"""
""" 2.
a = list(input().split())
print(max([int(i[::-1]) for i in a]))
"""
""" 3.
print(max([int(i[::-1]) for i in list(input().split())]))
"""
# 최종 형태
print(max([int(i[::-1]) for i in input().split()]))
