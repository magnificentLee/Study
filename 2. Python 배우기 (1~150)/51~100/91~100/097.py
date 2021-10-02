day = int(input())
num_list = map(int, input().split())
count = 0
for i in num_list:
    if i == day:
        count += 1
print(count)