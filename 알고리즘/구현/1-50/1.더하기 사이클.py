# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다.
# 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
#
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
n = int(input())
initial_n = n
count = 0
while True:
    start = n // 10  # 십의 자리
    end = n % 10  # 일의 자리
    result = start + end  # 십 + 일
    n = int(str(end) + str(result % 10))  # 새로운 수
    count += 1
    if n == initial_n:
        print(count)
        break