# 햄버거와 음료를 하나씩 골라, 세트로 구매하면,
# 가격의 합계에서 50원을 뺀 가격이 세트 메뉴의 가격이 된다.
"""
Input
800 : 상덕버거
700 : 중덕버거
900 : 하덕버거
198 : 콜라
330 : 사이다
Output
848 : 가장 싼 세트 메뉴
"""
""" 1차
import sys

b_list = []  # burger list
d_list = []  # drink list

for i in range(3):
    b = int(sys.stdin.readline())
    b_list.append(b)
for i in range(2):
    d = int(sys.stdin.readline())
    d_list.append(d)
price = min(b_list) + min(d_list) - 50
print(price)
"""
# 2차
m = 2000  # 모든 가격이 2천원 이하
b = 2000  # 동일
for i in range(3):
    n = int(input())
    m = min(n, m)

for j in range(2):
    n = int(input())
    b = min(n, b)

print(m + b - 50)