# 최종 답안 : try except 문으로 공백을 입력 받을시 종료되게끔
while True:
    try:
        n, m = input().split()
        flag = 0
        for i in range(len(m)):
            if m[i] == n[flag]:
                flag += 1
                if flag == len(n):
                    print("Yes")
                    break
        else:
            print("No")
    except:
        break
# 시도1 = 틀림 :계속 입력받는 경우를 간과한 경우
"""
n, m = input().split()
flag = 0
for i in range(len(m)):
    if m[i] == n[flag]:
        flag += 1
        if flag == len(n):  # 동일한 알파벳이 나와서 인덱스 길이를 초과하는 상황 방지
            break
if flag == len(n):
    print("Yes")
else:
    print("No")
"""
# 시도2 = 틀림 : 런타임 에러 발생, 원인 파악X
"""
while True:
    string = input()
    if not string:
        break
    n, m = string.split()
    flag = 0
    for i in range(len(m)):
        if m[i] == n[flag]:
            flag += 1
            if flag == len(n):
                print("Yes")
                break
    else:
        print("No")
"""