alp = [chr(i) for i in range(65, 91)]
for _ in range(int(input())):
    n = input()
    crypt = list(input())
    result = ""
    for i in n:
        if i == " ":
            result += i
        else:
            result += crypt[alp.index(i)]
    print(result)