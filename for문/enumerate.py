"""
import sys

score_list = []
for i in range(1, 9):
    n = int(sys.stdin.readline())
    score_list.append(n)
for j, s in enumerate(score_list):
    print(j, s)
score_lit = sorted(score_list)
for j, s in enumerate(score_lit):
    print(j, s)
결론 : j는 고유값이 아니기 때문에 s를 순서대로 나열해도 j는 변하지 않는다
"""