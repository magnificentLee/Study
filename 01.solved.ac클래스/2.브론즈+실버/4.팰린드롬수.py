# 팰린드롬 = 뒤에서 부터 읽어도 똑같은 단어 radar, sees 등등..
while True:
    n = int(input())
    result = 0
    if n == 0:
        break
    n_list = list(str(n))
    for i in range(len(n_list) - 1):
        if n_list[i] == n_list[len(n_list) - 1 - i]:
            continue
        else:
            result = -1
            break
    if result == -1:
        print("no")
    else:
        print("yes")