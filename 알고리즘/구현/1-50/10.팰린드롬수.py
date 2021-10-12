# 문자열을 활용
while True:
    n = input()
    if n == "0":
        break
    if n == n[::-1]:
        print("yes")
    else:
        print("no")

# 초기 작성
"""
while True:
    n = input()
    flag = 1
    if n == "0":
        break
    for i in range(len(n) // 2):
        if n[i] == n[-(i + 1)]:
            continue
        else:
            flag = 0
    if flag == 1:
        print("yes")
    else:
        print("no")
"""