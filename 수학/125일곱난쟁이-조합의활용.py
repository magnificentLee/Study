import sys

n_list = []

for i in range(9):  # 난쟁이 입력
    n_list.append(int(sys.stdin.readline()))
result = sum(n_list)
for i in range(9):
    for j in range(i + 1, 9):  # for i * for j = 조합(combination)
        if result - n_list[i] - n_list[j] == 100:   # i=4(15), j=8(25) 일 때 if문 탈출
            for k in range(9):  # k = 1,2,3...7,8
                if k == i or k == j:  # k = i(idx4= 15), j(idx8= 25) 는 continue
                    continue
                else:  # 예외들 k = 1,2,3,5,6,7(input : 7 8 10 13 19 20 23)
                    print(n_list[k])  # 출력
            exit()
