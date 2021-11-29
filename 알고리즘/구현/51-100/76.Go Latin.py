table = {"a": "as", "i": "ios", "y": "ios", "l": "les", "n": "anes", "ne": "anes",
         "o": "os", "r": "res", "t": "tas", "u": "us", "v": "ves", "w": "was"}
t = int(input())
for _ in range(t):
    n = input()
    l = len(n)
    tmp = ""
    if n[-1] in table:
        for i in range(l - 1):
            tmp += n[i]
        tmp += table[n[-1]]
    elif n[-2] + n[-1] == "ne":
        for i in range(l - 2):
            tmp += n[i]
        tmp += table[n[-2] + n[-1]]
    else:
        tmp = n + "us"
    print(tmp)