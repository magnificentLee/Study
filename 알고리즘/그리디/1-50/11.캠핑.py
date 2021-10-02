# 연속하는 P일 : 일주일 개념으로 생각
# L : 캠핑장에서 지내는 날
# V : 전체 휴가 일수
# V // P = 캠핑장을 빌리는 주간, 2일 경우 2주동안 빌리는것
# V % P = 2 주간 빌리고 남는 낱개일 수
# 위 식을 바탕으로 작성하자
i = 1
while True:
    L, P, V = map(int, input().split())
    result = 0
    if L == 0:
        break
    result += (V // P) * L
    if V % P >= L:  # P주차(V//P*L) 더 못하지만 L일 더 지낼 수 있기 때문
        result += L
    else:  # P주차 X L일도 X, 따라서 나머지 만큼만 더 보낼 수 있음(나머지는 L보다 작음)
        result += V % P
    print("Case {}: {}".format(i, result))
    i += 1
