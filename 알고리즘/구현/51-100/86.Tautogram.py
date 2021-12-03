# 예상 이상으로 시간이 걸렸기 때문에 중간에 중단 장치가 필요하다고 판단됨
# 길이 비교가 아닌 T/F 판별로 해보자
# 결국 모든 단어들의 시작지점은 처음과 같아야하므로 인덱스를 앞뒤로 비교해주는게 아닌 처음과 비교해주는 방식으로하자
# 방식 비교자체는 영향이 없었음
# 빠른 입력을 사용하니 절반이상 줄어들었음
from sys import stdin
input = stdin.readline

while True:
    n = input().split()
    start = n[0][0].capitalize()
    if start == "*":
        break
    flag = 1
    for i in n:
        if start != i[0].capitalize():
            flag = 0
            break
    if flag == 1:
        print("Y")
    else:
        print("N")

# 공백 기준으로 끊어서 시작부분을 비교, 대 소문자는 서로 다르기 때문에 하나로 통일시켜줄것
# 굳이 if문으로 확인 안 하고 대문자화 해도 상관없을듯
# 길이는 최대 20자 밖에 안 되므로 중간에 break 할 필요는 없을 것 같음
"""
while True:
    n = input().split()
    l = len(n)
    if n[0] == "*":
        break
    flag = 1
    for i in range(1, l):
        if n[i - 1][0].capitalize() == n[i][0].capitalize():
            flag += 1
    if flag == l:
        print("Y")
    else:
        print("N")
"""