# 남자 : 받은 수의 배수
# 여자 : 선택지 좌우 대칭으로 비교, 만약 좌우가 서로 다르다면 현재 위치만 변경, 좌우가 같다면 좌우의 좌우도 비교... 대칭이 끝나면
# 해당 위치의 상태를 전부 변경 => 전체 상태의 갯수는 홀수일 필요가 있음
# 남자의 경우는 쉽지만 여자의 경우 인덱스 초과가 발생할 가능성이 높음
# 여자는 주어지는 스위치를 기준으로 좌우 대칭을 비교하기 때문에 전체 길이의 절반까지만 반복문을 돌려주자
def male(s):
    for j in range(s, n + 1, s):
        switch(j)
    return

def female(s):
    switch(state)
    # state(시작점)의 경우 switch(start), switch(end) 두 번을 돌면서 원상복귀 되므로 1부터 시작
    # 그 대신 반복문 시작전 시작점(state)의 상태를 바꿔줌
    for j in range(1, n // 2):
        start = s - j
        end = s + j
        if start < 1 or end > n:
            break
        if array[start] == array[end]:
            switch(start)
            switch(end)
        else:
            break
    return

def switch(s):
    if array[s] == 0:
        array[s] = 1
    else:
        array[s] = 0
    return


n = int(input())
array = [-1] + list(map(int, input().split()))  # [-1] = 인덱스 맞춤용 허수
t = int(input())
for _ in range(t):
    gender, state = map(int, input().split())
    # 여기부터 문제, 인덱스를 어떻게 조절해야될까
    # 처음 주어진 값은 1부터 시작하는 값임, 단순히 state -= 1 처리하기에는 남자쪽에서 배수 3, 6, 9.. 가 아닌 2, 4, 6...으로
    # 변하기 때문에 단순히 -1 처리할 문제가 아님
    if gender == 1:
        male(state)
    else:  # gender == 2
        female(state)
for i in range(1, n + 1):
    print(array[i], end=" ")
    if i % 20 == 0:
        print()