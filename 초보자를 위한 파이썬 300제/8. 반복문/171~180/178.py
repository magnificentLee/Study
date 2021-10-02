my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1): # 결과는 3줄, 리스트는4개 따라서 -1
    print(abs(my_list[i + 1] - my_list[i]))