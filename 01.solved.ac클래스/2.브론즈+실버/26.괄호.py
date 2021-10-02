t = int(input())

for _ in range(t):
    n = input()
    stack = []
    result = True
    for i in n:
        if i == "(":
            stack.append(i)
        else:  # if i == ")"
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                result = False
    if result and stack == []:
        print("YES")
    else:
        print("NO")
