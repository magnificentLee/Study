n = int(input())
num_list = list(map(int, input().split()))
score = 0
a = 0
for i in range(n):
    if num_list[i] == 1:
        a += 1
        score += a
    else:
        a = 0
print(score)