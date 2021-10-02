# 추가로 볼 필요 있음
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start  # 처음값, array[0]
    left = start + 1  # 처음값 이후, array[1:]
    right = end  # 가장 끝 값, len(array) - 1
    while left <= right:
        while left <= end and array[left] <= array[pivot]:  # 기준보다 작으면
            left += 1
        while right > start and array[right] >= array[pivot]: # 기준보다 크면
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 기준값을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array) - 1)
print(array)