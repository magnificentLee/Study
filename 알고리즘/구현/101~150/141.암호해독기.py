# 평문을 암호로 바꿨을때(대문자 1~26  소문자 27~52) 암호문과 일치하는지를 물어보는 문제
# 암호문은 순서를 섞어놓았다는 점에 주의
# 값의 범위가 넓다 따라서 빠른 입출력을 사용하자
# 대문자 65~90 소문자 97~122
# 대문자 1~26  소문자 27~52
import sys

n = int(input())
code = sorted(map(int, sys.stdin.readline().rstrip().split()))  # 암호문
clear_text = input()  # 평문
def change(m):
    c = ord(m)
    if 65 <= c <= 90:
        c -= 64
    elif 97 <= c <= 122:
        c -= 70
    else:
        c = 0
    return c


array = sorted([change(i) for i in clear_text])
for i in range(n):
    if code[i] != array[i]:
        print("n")
        break
else:
    print("y")