data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]
for i in data: #20~19:1 / 75~19:2 / 15~14:3
    for j in i: # 2000~1980:4 / 7500~1980:4 / 15~14:4
        print(j * 1.00014)
    print("-" * 5)