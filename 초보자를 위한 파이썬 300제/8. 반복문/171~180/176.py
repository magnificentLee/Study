my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list) - 2): # 결과가 3줄, 리스트는 5개이므로 -2
    print(my_list[i], my_list[i + 1], my_list[i + 2])