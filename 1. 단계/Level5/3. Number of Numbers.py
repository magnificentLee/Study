a = int(input())
b = int(input())
c = int(input())

total = a * b * c
count_list = list(str(total))
for i in range(10):
    num_count = count_list.count(str(i))
    print(num_count)