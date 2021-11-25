# a mod b : a % b 라는 뜻
# 문제를 잘못 이해해서 풀었던 경우

# 공식자체만 보자, L,O,V,E 의 갯수만 카운트해서 계산하면 된다
# 예제에 LOVE와 다른 이름이 나왔다고 이름이 바뀌는 경우마다 계산할 필요가 없다는 뜻이다
# 공식 잘못이해해서 풀던 코드 수정함
# 각이름 + 팀에서 L,O,V,E 의 갯수를 카운트한 값을 L,O,V,E 라고 한다면
# 확률 = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100 가 기본 공식임
# 이름이 JAKE 라고 L이 J로 바뀌는 그런게 아님!!

name = input()
t = int(input())
max_tmp = 0
team = sorted([[input(), 0] for _ in range(t)])
for i in range(t):
    tmp = name + team[i][0]
    formula_count = []
    for j in "LOVE":
        formula_count.append(tmp.count(j))
    result_tmp = []
    for j in range(4):
        for k in range(j + 1, 4):
            front = formula_count[j] + formula_count[k]
            result_tmp.append(front)
    percent = 1
    for j in result_tmp:
        percent *= j
    team[i][1] = percent % 100
team = sorted(team, key=lambda x: x[1], reverse=True)
print(team[0][0])

# 아래로 공식을 잘못이해한 경우들임
# 이름이 바뀔때 마다 계산하는 코드
"""
name = input()
t = int(input())
max_tmp = 0
team = sorted([[input(), 0] for _ in range(t)])
for i in range(t):
    tmp = name + team[i][0]
    count = [0] * 26
    for j in set(tmp):
        count[ord(j) - 65] = tmp.count(j)
    result_tmp = []
    for j in range(len(name)):
        for k in range(j + 1, len(name)):
            front_val = count[ord(name[j]) - 65] + count[ord(name[k]) - 65]
            result_tmp.append(front_val)
    front = 1
    for j in result_tmp:
        front *= j
    team[i][1] = front % 100
    print(team[i][0], result_tmp)
"""

# 중복되는 경우, 팀이 하나만 주어지는 경우 오답 or 에러 발생하는 코드
"""
name = input()
t = int(input())
max_tmp = 0
for _ in range(t):
    team = input()
    tmp = name + team
    count = [0] * 26
    for i in set(tmp):
        count[ord(i) - 65] = tmp.count(i)
    result_tmp = []
    for i in range(len(name)):
        for j in range(i + 1, len(name)):
            front_val = count[ord(name[i]) - 65] + count[ord(name[j]) - 65]
            result_tmp.append(front_val)
    print(result_tmp)  # 제거
    front = 1
    for i in result_tmp:
        front *= i
    front %= 100
    print(front)  # 제거
    if front > max_tmp:
        max_tmp = front
        max_team = team
print(max_team)
"""