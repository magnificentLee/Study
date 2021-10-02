"""
테스트 케이스 갯수가 주어지지 않는 것에 유념
try except : try에 대한 에러(a 1, 3, 2, ㄱ 입력) 발생시 break로 while문 중단
각 케이스가 계속 진행되뎌 마지막에 대한 언급이 없기 때문에 이에 유의한다
"""
import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break
