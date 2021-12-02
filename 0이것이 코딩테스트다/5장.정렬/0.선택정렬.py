# 인덱스0(시작값)과 값을 비교해가며 가장 낮은 값을 찾아 인덱스 0과 교환
# 인덱스1과... 같은 과정을 반복하여 정렬하는 방식
# 최선 평균, 최악 모두 n^2 의 시간복잡도를 가짐

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)