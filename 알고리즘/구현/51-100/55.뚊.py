# 가로로 2배 늘리는 것이므로 2배 늘려서 리스트에 저장한 뒤 비교해주면 될듯
n, m = map(int, input().split())
start = []
flag = 0
for _ in range(n):
    a = input()
    tmp = ""
    for i in a:
        tmp += i * 2
    start.append(tmp)
for i in range(n):
    b = input()
    if start[i] == b:
        flag += 1
if flag == len(start):
    print("Eyfa")
else:
    print("Not Eyfa")
