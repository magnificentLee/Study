# ZeroDivisionError 때문에 try except 문을 사용하여 여러번 바꿔봤으나 채점 시작도전에 틀렸습니다가 나왔음
# 오답 원인을 찾자면
# 1. ZeroDivisionError 를 생각하지 않고 코드를 짠 것
# 다음부턴 변수를 이용해 나누는 과정이 있을 경우 해당 에러를 고려해야할것임
# 2. 최다 득점, 최다 실점을 기준으로 답을 구한것(sorted 람다를 이용)
# 최다 득점, 최다 실점이 아닌데도 피타고라스 최댓값, 최솟값이 나오는 경우의 수가 분명히 있을 것임
# 따라서 득점을 기준으로 리스트를 만들어 리스트에서 최댓값, 최솟값을 찾아 출력했음
# 1428ms 의 시간이 걸리기 때문에 입력값의 범위가 더 넓어진다면 해당 방법을 사용할 수 없을 것
for _ in range(int(input())):
    n, m = map(int, input().split())
    teams = [[0, 0] for i in range(n)]  # 득점, 실점
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        teams[a - 1][0] += p
        teams[a - 1][1] += q
        teams[b - 1][0] += q
        teams[b - 1][1] += p
    teams_total = []
    for i in range(n):
        if teams[i][0] == 0 and teams[i][1] == 0:
            teams_total.append(0)
        else:
            res = (teams[i][0] ** 2 / (teams[i][0] ** 2 + teams[i][1] ** 2)) * 1000
            teams_total.append(res)
    print(int(max(teams_total)), int(min(teams_total)), sep="\n")
# 최초 풀이 : ZeroDivisionError 발생
"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    teams = [[i, 0, 0] for i in range(n)]
    for i in range(m):
        a, b, p, q = map(int, input().split())
        teams[a - 1][1] += p
        teams[a - 1][2] += q
        teams[b - 1][1] += q
        teams[b - 1][2] += p
    teams = sorted(teams, key=lambda x: x[1], reverse=True)
    res_max = (teams[0][1] ** 2 / (teams[0][1] ** 2 + teams[0][2] ** 2)) * 1000
    res_min = (teams[-1][1] ** 2 / (teams[-1][1] ** 2 + teams[-1][2] ** 2)) * 1000
    print(int(res_max), int(res_min), sep="\n")
"""
# ZeroDivisionError 가 아닌 최초로 틀렸습니다를 출력
"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    teams = [[i, 0, 0] for i in range(n)]
    for i in range(m):
        a, b, p, q = map(int, input().split())
        teams[a - 1][1] += p
        teams[a - 1][2] += q
        teams[b - 1][1] += q
        teams[b - 1][2] += p
    teams = sorted(teams, key=lambda x: x[1], reverse=True)
    try:
        res_max = (teams[0][1] ** 2 / (teams[0][1] ** 2 + teams[0][2] ** 2)) * 1000
        res_min = (teams[-1][1] ** 2 / (teams[-1][1] ** 2 + teams[-1][2] ** 2)) * 1000
    except:
        res_max = 0
        res_min = 0
    print(int(res_max), int(res_min), sep="\n")
"""
# 해당 코드를 통해 기존의 최다 득점, 최다 실점을 이용해 구하는 방법이 잘못된 것임을 파악함
"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    teams = [[0, 0] for i in range(n)]
    for i in range(m):
        a, b, p, q = map(int, input().split())
        teams[a - 1][0] += p
        teams[a - 1][1] += q
        teams[b - 1][0] += q
        teams[b - 1][1] += p
    teams_total = []
    try:
        for i in range(n):
            res = (teams[i][0] ** 2 / (teams[i][0] ** 2 + teams[i][1] ** 2)) * 1000
            teams_total.append(res)
    except:
        teams_total.append(0)
    print(int(max(teams_total)), int(min(teams_total)), sep="\n")
"""