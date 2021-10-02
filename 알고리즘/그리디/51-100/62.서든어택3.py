from sys import stdin

input = stdin.readline


def game(array):
    joon = array.pop(0)
    # others = array.sort()  # 여기서 NoneType을 return 하는 것 같음(정답)
    array.sort()
    for i in array:
        if joon <= i:
            return 0
        else:
            joon += i
    else:
        return 1


n = int(input())
players = list(map(int, input().split()))
result = game(players)
if result == 0:
    print("No")
else:
    print("Yes")