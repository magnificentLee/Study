num_list = list(map(int, input().split()))
total = 0

for i in num_list:
    total += i ** 2

print(total % 10)
