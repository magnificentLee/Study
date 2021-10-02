# 설명을 뭣같이 써놓긴 했는데
# 풀어보면 리스트에서 몇 번쨰로 낮은 값인지(idx:0 ~) 출력하라는 것
"""
from sys import stdin
n = int(stdin.readline())
num1 = list(map(int, stdin.readline().split()))
num2 = list(sorted(set(num1)))
num_dic = {value: index for index, value in enumerate(num2)}
print(num_dic)
for i in num1:
    print(num_dic[i], end=" ")
"""
from sys import stdin
n = int(input())
arr = list(map(int, stdin.readline().split()))
arr_set = sorted((set(arr)))
arr_dic = {value: index for index, value in enumerate(arr_set)}
for i in arr:
    print(arr_dic[i], end=" ")

# 시도1 : 시간초과 발생
# 원인은 값을 하나씩 비교하는 방식이기 때문에 N의 범위가 백만까지, 따라서 백만 * 백만 = 1조
# 추정치 1조의 연산을 수행하기 때문에 발생하는 것이라고 추측됨
"""
from sys import stdin
n = int(stdin.readline())
val = list(map(int, stdin.readline().split()))
res_list = []
for i in val:
    result = 0
    for j in set(val):
        if i > j:
            result += 1
    res_list.append(result)
print(*res_list)
"""