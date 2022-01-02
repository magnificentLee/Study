# 중복 확인 : set
# 사이클 배열 인덱스 : (i % number) 로 활용 가능

for _ in range(int(input())):
    n = int(input())  # 아이들 숫자
    array = list(map(int, input().split()))  # 아이들 리스트
    h = [0] * n
    count = 0

    while True:
        #if len(set(array)) == 1:  # 시작할 때 짝/홀수를 판별하여 미리 사탕을 나눠주기 때문에 판별 이후에 정지조건을 넣는게 맞음
        #    print(count)
        #    break
        for i in range(n):  # 홀수일때 사탕 보충
            if array[i] % 2 == 1:
                array[i] += 1
            h[i] = array[i] // 2  # 절반값의 리스트(다음 인덱스값에 더해줄예정)

        if len(set(array)) == 1:
            print(count)
            break

        for i in range(1, n):
            array[i] = array[i] // 2 + h[i - 1]
        array[0] = array[0] // 2 + h[-1]  # 원형이므로 시작값은 끝값을 더해야함
        count += 1