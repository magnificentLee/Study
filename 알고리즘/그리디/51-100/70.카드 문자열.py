# 파이썬은 문자열 그대로를 아스키코드에 대응해서 값을 비교함
# 따라서 ord 혹은 chr 을 이용할 필요가 없을것
# 함수
def sorting(n, array):
    start = array[0]
    result = [start]
    for i in range(1, n):
        if start >= array[i]:  # 시작값보다 작으면 왼쪽
            start = array[i]  # 제일 중요, 놓친 부분
            result.insert(0, array[i])
        else:  # 시작값보다 크면 오른쪽 정렬
            result.append(array[i])
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    card = list(input().split())
    print(*sorting(n, card), sep="")
# 처음 작성한 코드
"""
t = int(input())
for _ in range(t):
    n = int(input())
    card = list(input().split())
    start = card[0]
    result = [card[0]]
    for i in range(1, n):
        if start >= card[i]:
            start = card[i]  # 추가 완료
            result.insert(0, card[i])
        else:
            result.append(card[i])
    print(*result, sep="")
"""