n = int(input())
answer = 1
for i in range(1, n + 1):  # 1~n 까지
    answer *= i
print(answer)