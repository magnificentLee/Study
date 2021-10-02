n = 1
for i in range(3):
    n *= int(input())
n_list = list(map(int, str(n)))
for i in range(10):
    print(n_list.count(i))
""" 
2달전 코드
a = int(input())
b = int(input())
c = int(input())

total = a * b * c
count_list = list(str(total))
for i in range(10):
    num_count = count_list.count(str(i))
    print(num_count)
--------------------------------------------
1달전 코드
a = int(input())
b = int(input())
c = int(input())

answer = a * b * c
for i in range(10):
    num_count = list(str(answer)).count(str(i))
    print(num_count)
"""