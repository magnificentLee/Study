# 201000 이라는 숫자가 있을 때 오른쪽에서 봤을 때
# 0 0 0 1 0 2, 처음으로 0이 아닌 숫자는 4번 째이므로 그 전의 0의 개수는 3개
# 10! = 3628800 -> 0088263, 0이 아닌 처음수 3번째, 까지의 0개수 = 2
n = int(input())
total = 1
count = 0
for i in range(1, n + 1):
    total *= i
total_reverse = str(total)[::-1]
for j in total_reverse:
    if j != "0":
        break
    count += 1
print(count)