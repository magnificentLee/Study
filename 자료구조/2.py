from 자료구조.Stack_queue import Stack  # 스택 클래스 가져오기


def parChecker(parSeq):
    S = Stack()  # 괄호 쌍을 쌓아둘 빈 스택 공간 준비
    for i in parSeq:  # 임의의 괄호들로 이루어진 문자열에서..
        if i == '(':  # 일단 무조건 왼쪽괄호가 나오면
            S.push(i)  # 스택에 넣어준다
        else:  # 만약 오른쪽괄호가 먼저 나오면?
            if len(S) == 0:
                return False  # 쌍이 안맞는다
            else:
                S.pop()  # 쌍이 맞으면, pop을 통해 스택을 비운다
    if len(S) == 0:
        # if S.isEmpty(): 를 대신 사용할 수도 있다
        return True  # 스택 내 item이 없이 깔끔하면 True
    else:
        return False


A = input()
print(parChecker(A))
# (()()) : True
# (()))( : False