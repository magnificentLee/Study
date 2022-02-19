# 8 7 6 5 4 3 2 1 이라는 요소를 가지는 리스트가 있다고 가정
# 병합의 원리는 8 7 6 5 / 4 3 2 1 로 나누고 8 7/ 6 5/ 4 3/ 2 1 로 나눠서 7 8/ 5 6/ 3 4/ 1 2
# 다시 합치는 과정 5 6 7 8/ 1 2 3 4 -> 1 2 3 4 5 6 7 8
# 즉, 비교 할 수 있는 최소 단위(리스트당 요소 2개)로 나누어 크기 순으로 정렬한 다음 다시 합치는 과정에서
# 크기를 비교하며 정렬하는 것
# 모든 상황에서 nlogn의 시간복잡도를 가지며 힙 정렬과 동일함 (최선의 경우 팀 정렬이 n으로 더 빠름)


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    small_part_left = merge_sort(left)
    small_part_right = merge_sort(right)
    return merge(small_part_left, small_part_right)

def merge(lt, rt):
    i, j = 0, 0
    sorted_list = []
    while i < len(lt) and j < len(rt):
        if lt[i] < rt[j]:
            sorted_list.append(lt[i])
            i += 1
        else:
            sorted_list.append(rt[j])
            j += 1
    while i < len(lt):
        sorted_list.append(lt[i])
        i += 1
    while j < len(rt):
        sorted_list.append(rt[j])
        j += 1
    return sorted_list


initial_list = list(map(int, input().split()))
print(*merge_sort(initial_list))
# 입력 : 아무렇게나 리스트로, ex) 8 7 6 5 4 3 2 1