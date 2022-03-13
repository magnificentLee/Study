# range를 이용해 특정 범위의 딕셔너리 리스트를 만드는 방법
check_list = {i + 1: 0 for i in range(9)}
check_list[1] += 1
check_list[9] += 1
print(check_list)

# output
# {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1}