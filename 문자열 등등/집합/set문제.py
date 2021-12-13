# 백준 11723
# 시간, 메모리 제한이 빡빡한 문제
# remove로 존재하지 않는 요소를 지우려고 시도할 경우 keyerror가 발생함

from sys import stdin
input = stdin.readline

s = set()
for i in range(int(input())):
    b = input().split()  # all, empty 때문에 시작 변수는 하나만 가능
    if len(b) == 1:
        if b[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        string, n = b[0], int(b[1])
        if string == "add":
            s.add(n)
        elif string == "remove":
            s.discard(n)  # remove를 쓸 경우 keyerror가 발생함
        elif string == "toggle":
            if n in s:
                s.remove(n)  # remove를 써도 통과 됨 아마 remove는 없는 값을 시도할 경우 에러가 나오는것 같음
            else:
                s.add(n)
        else:  # check
            if n in s:
                print(1)
            else:
                print(0)