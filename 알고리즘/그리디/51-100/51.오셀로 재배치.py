def othello(n, array1, array2):
    white = 0
    black = 0
    for i in range(n):
        if array1[i] != array2[i]:
            if array1[i] == "B":
                white += 1
            else:
                black += 1
    # BBBBBBB                   WWBB
    # BWBWBWB                   BBWB
    # 일 때 0이 나오는 것을 방지 /  일 때 1 이 나오는 것을 방지
    if white >= black:
        return white
    else:
        return black


t = int(input())
for i in range(t):
    n = int(input())
    ot1 = list(input())
    ot2 = list(input())
    print(othello(n, ot1, ot2))
