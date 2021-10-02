a = int(input())
b = int(input())
c = int(input())

answer = a * b * c
for i in range(10):
    num_count = list(str(answer)).count(str(i))
    print(num_count)
