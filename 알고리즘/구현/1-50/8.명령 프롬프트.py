# 다음 문자열과 비교하여 원소의 값이 다르면 ? 로 바꿔주면 될듯
n = int(input())
string = [list(input()) for _ in range(n)]
start = string[0]
for i in range(n):
    for j in range(len(start)):
        if start[j] != string[i][j]:
            start[j] = "?"
print(*start, sep="")