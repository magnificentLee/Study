# 문장 위 아래가 다르게 돌아가게 만들자 (병의 단수 복수 형태에 주의)
# 끝에 "." 빼먹어서 틀림
n = int(input())
flag = "Take one down and pass it around"
b = "bottles"
b_single = "bottles"
for i in range(n, -1, -1):
    if i > 1:
        idx = i - 1
        b_single = "bottles"
        if idx == 1:
            b_single = "bottle"
    elif i == 1:
        idx = "no more"
        b = "bottle"
        b_single = "bottles"
    elif i == 0:
        flag = "Go to the store and buy some more"
        i = "no more"
        b = "bottles"
        b_single = "bottles"
        if n == 1:
            b_single = "bottle"
        idx = n
    print("{} {} of beer on the wall, {} {} of beer.".format(str(i).capitalize(), b, i, b),
          "{}, {} {} of beer on the wall.".format(flag, idx, b_single), sep="\n")
    print()