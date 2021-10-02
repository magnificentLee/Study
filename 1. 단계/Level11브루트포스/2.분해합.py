n = int(input())
for i in range(1, n + 1):
    # i를 문자열로 만든후 각각의 숫자를 정수형으로 리스트화
    n_list = list(map(int, str(i)))
    result = i + sum(n_list)
    if result == n:
        print(i)
        break
    if i == n:  # 생성자가 없는 경우
        print(0)
        # for문의 마지막 숫자이기 때문에 break 필요 없음
