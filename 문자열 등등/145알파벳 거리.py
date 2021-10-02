# 문자 -> 아스키코드 : ord
t = int(input())

for i in range(t):
    a, b = input().split()
    list_a = list(a)
    list_b = list(b)
    ord_a = []
    ord_b = []
    result = ""
    for j in range(len(a)):
        ord_a.append(ord(list_a[j]))
        ord_b.append(ord(list_b[j]))
    for k in range(len(a)):
        if ord_b[k] >= ord_a[k]:
            result += str(ord_b[k] - ord_a[k]) + " "
        else:
            result += str((ord_b[k] + 26) - ord_a[k]) + " "
    print("Distances: " + result.rstrip())
