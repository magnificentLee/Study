"""
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)
"""
# 만약 복수의 입력을 받아야 한다면
from sys import stdin as st
from sys import stdin as sd
a = st.readline().rstrip()
b = sd.readline().rstrip()
print(a, b, end="\n")
# 테스트 결과 하나만 가능한걸로 판단됨
# 복수개 입력은 이게 아닐것