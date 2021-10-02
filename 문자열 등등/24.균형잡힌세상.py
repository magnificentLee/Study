# (,),[,] 이 들어간 경우, " ." 이 들어간 경우를 생각해야됨
# 전자만 고려할 경우 후자의 경우 결과값이 제대로 나오지 않을 것임
# 따라서 두 가지 조건을 만족하는 경우 통과하게끔 작성하자
while True:
    n = input()
    if n[0] == ".":  # 종료 조건
        break
    stack = []
    result = True  # 괄호가 없는 경우, 괄호 닫음만 나오는 경우의 통과를 위함
    for i in n:
        if i == "(" or i == "[":  # 스택엔 괄호 열음을 추가
            stack.append(i)
        elif i == ")":  # 스택에 들어간 괄호와 비교
            # 스택이 빈 경우 인덱스 초과오류를 방지하기 위해 stack and 조건이 추가됨
            if stack and stack[-1] == "(":
                stack.pop()  # 스택에 들어간 괄호를 후입선출하는 방식
            else:
                result = False
        elif i == "]":
            # 스택이 빈 경우 인덱스 초과오류를 방지하기 위해 stack and 조건이 추가됨
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                result = False
    if result and stack == []:  # 최종적으로 스택이 빈 경우 통과
        print("yes")
    else:
        print("no")
# 고쳐야 될 점
# m )( a trail in a maze. 이렇게 들어가는 경우
# 라인 14에서 인덱스 초과 오류가 난다
# 리스트 안에 요소가 하나라도 있을 경우 문제가 없지만
# 비어있을 경우 인덱스 오류가 반드시 발생하기 때문에 이를 고려해줘야 한다.
# 참고한 코드
"""
import sys
input = sys.stdin.readline
while 1:
    string = input().rstrip()
    stack = []
    true_flag = 1
    for cha in string:
        if cha == '(' or cha == '[':
            stack.append(cha)
        elif cha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                true_flag = 0
                break
        elif cha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break
    if string == '.':
        break
    print("yes" if true_flag and not(stack) else "no")
"""