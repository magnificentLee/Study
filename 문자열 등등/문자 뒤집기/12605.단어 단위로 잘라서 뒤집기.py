for i in range(1, int(input()) + 1):
    n = input().split()
    # split을 통해 단어 단위로 리스트화 시키는게 중요함
    # list(input())으로 처리하면 알파벳 단위로 잘라서 출력하기 때문에 단어 각각도 뒤집힌채 출력됨
    tmp = ""
    for j in range(len(n) - 1, -1, -1):
        tmp += n[j]
        tmp += " "
    print("Case #{}: {}".format(i, tmp))
