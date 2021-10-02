from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    coupons_needs = []  # 상금으로 교환할 때 필요한 쿠폰의 인덱스 리스트
    coupons_type = {}  # 각 쿠폰의 누적치
    prize_list = []  # 상금 리스트
    for i in range(m):
        coupons_type[i + 1] = 0
    for _ in range(n):
        a = list(map(int, input().split()))
        a.pop(0)  # 스티커의 개수 제거(필요없음)
        # prize = a.pop() 을
        # prize_list.append 와 합칠 경우 None 값을 추가하므로 런타임 에러가 발생할것임
        prize = a.pop()  # 상금 리스트용
        coupons_needs.append(a)  # 필요한 부분 제거한 리스트를 저장
        prize_list.append(prize)  # 상금 리스트에 추가
    coach = list(map(int, input().split()))  # 코치가 가진 쿠폰 수량들 리스트
    for i, j in enumerate(coach):  # i = 쿠폰 인덱스, j = 쿠폰 수량
        coupons_type[i + 1] += j  # 쿠폰 딕셔너리의 밸류값을 추가
    result = 0
    for i in range(n):
        val = []  # 이중 리스트에서 개별 리스트의 인덱스 밸류값 리스트
        for j in range(len(coupons_needs[i])):  # 개별 리스트 길이 만큼 실행
            val.append(coupons_type[coupons_needs[i][j]])  # 개별 리스트에 해당하는 밸류값을 리스트에 추가
        result += min(val) * prize_list[i]  # 최솟값 만큼 뽑아 낼 수 있기 때문에 최솟값 * 상금을 결과에 추가
    print(result)
