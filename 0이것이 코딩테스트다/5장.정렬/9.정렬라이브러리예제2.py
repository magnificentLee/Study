# 방법1
"""
t = int(input())

array = [input().split() for i in range(t)]
array.sort(key=lambda x: x[1])
for i in range(t):
    print(array[i][0], end=" ")
"""
# 방법2 (방법1 출력 방식 수정)
"""
t = int(input())

array = [input().split() for i in range(t)]
array.sort(key=lambda x: x[1])
for i in array:
    print(i[0], end=" ")
"""
# 방법3 교재방식
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))
array = sorted(array, key= lambda student: student[1])
for student in array:
    print(student[0], end=" ")
