# 데이터의 크기와 범위가 제한된 경우에서 사용가능, 가장 빠름
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 인덱스 값에 해당하는 크기를 증가해야됨 따라서 전체 값을 포함하는 리스트를 생성
# 즉, len(array) 가 아닌 max(array) + 1
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]): # 1 = 2개이므로 2번, 7 = 1개이므로 1번
        print(i, end=" ")
