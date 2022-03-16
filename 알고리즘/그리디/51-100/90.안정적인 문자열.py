# 각 테스트 케이스마다 출력하는게 아님
# 반복문 종료후 최종적으로 한 번에 출력하는 것
idx = 0
while True:
    idx += 1
    n = input()
    stack = []
    count = 0
    if "-" in n:
        break
    for i in range(len(n)):
        if not stack and n[i] == "}":
            count += 1
            stack.append("{")
        elif stack and n[i] == "}":
            stack.pop()
        else:
            stack.append("{")
    count += len(stack) // 2
    print("{}. {}".format(idx, count))