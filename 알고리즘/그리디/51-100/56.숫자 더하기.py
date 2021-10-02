while True:
    vals = list(map(int, input().split()))
    n = vals[0]
    if n == 0:
        break
    zero = vals.count(0)
    nums = sorted(vals[1:])
    left, right = "", ""
    # 0 이 존재할경우 제일 앞에 정렬된 수 = 0 따라서 0 카운트만큼부터 시작하면 0 다음 숫자가 나옴
    for i in range(zero, n):  # 2를 나눈 나머지 존재 = 왼쪽추가 / 존재X = 오른쪽 추가
        if (zero - i) % 2 == 0:
            left += str(nums[i])
        else:
            right += str(nums[i])
    new_left = left
    new_right = right
    for i in range(zero):
        if len(left) == len(right):
            if i % 2 == 0:
                new_left = new_left[0] + "0" + new_left[1:]
            else:
                new_right = new_right[0] + "0" + new_right[1:]
        else:
            if i % 2 == 0:
                new_right = new_right[0] + "0" + new_right[1:]
            else:
                new_left = new_left[0] + "0" + new_left[1:]
    print(int(new_left) + int(new_right))