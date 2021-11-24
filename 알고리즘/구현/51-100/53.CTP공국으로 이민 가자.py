# A = 1 : 65  => 65 - 64
# Z = 90 => 90 - 64 = 26
# ord("A"), chr(65)
for _ in range(int(input())):
    n, m = input().split()
    array = input().split()
    if m == "C":
        for i in array:
            print(ord(i) - 64, end=" ")
    elif m == "N":
        for i in array:
            # chr로 변환시 str 값으로 출력됨
            tmp = chr(int(i) + 64)
            print(tmp, end=" ")
    print()

