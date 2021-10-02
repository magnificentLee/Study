apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print("{} 호".format(j), "-----", sep="\n")
        # 또는
        # print(j, "호")
        # print("-" * 5)