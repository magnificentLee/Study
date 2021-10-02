"""
3    # 전체 테스트 케이스 개수
1 0  # 문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇 번째에 놓여 있는지 M
5    # N개의 문서의 중요도 차례대로
4 2  # N, M
1 2 3 4
6 0  # N, M
1 1 9 1 1 1
OUTPUT  # 문서가 몇 번째로 인쇄되는지
1
2  (12*4) - > (412*) - > (4*12) : *의 위치 = 2
5  (19111*) -> (9111*1) : *의 위치 = 5
"""
"""
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print_list = list(map(int, input().split()))
    prior_number = []

    for doc in print_list:
        prior_number.append(doc)

    result = [0 for _ in range(n)]
    queue = [i for i in range(n)]
    sequence = 1
    while queue:
        if print_list[queue[0]] == max(prior_number):
            prior_number.remove(max(prior_number))
            result[queue.pop(0)] = sequence
            sequence += 1
        else:
            queue.append(queue.pop(0))
    print(result[m])
"""
# imp의 첫번째 값이 최댓값이 될 때까지 가장 첫번째 값을 맨 뒤로 보내는 FIFO를 반복
# 첫번째 값이 최댓값이 되면 order를 하나 증가
# 원래 문서의 인덱스를 idx에 저장하고 imp의 순서가 바뀔 때 마다 같이 순서를 바꿔줘야 함
# 그래야 원래 m 번째 문서가 언제 출력되는지 알 수 있음
"""
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = "target"

    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1

            if idx[0] == "target":
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
"""
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(range(n))
    idx[m] = "target"
    result = 0
    while True:
        if imp[0] == max(imp):  # target은 크기 비교가 불가능하기 때문에 idx 리스트를 추가로 만든것
            result += 1
            if idx[0] == "target":
                print(result)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))