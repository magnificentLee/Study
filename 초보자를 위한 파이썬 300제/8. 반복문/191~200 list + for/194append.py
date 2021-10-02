data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]
result = []
for i in data:
    result_sub = []
    for j in i:
        result_sub.append(j * 1.00014)  # result_sub를 채움
    result.append(result_sub)  # result를 result_sub로 채움
print(result)
