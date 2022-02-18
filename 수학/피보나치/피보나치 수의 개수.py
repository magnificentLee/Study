# 백준 6571
# a부터 b까지의 피보나치 개수를 구하는 문제
# 여러번 실패했는데 실패 원인은
# 처음 생각했던 원인은 while문 때문에 recursion error가 걸린것 같음 => X

# 최종적으로 확인한 원인들
# 1. 문제에 주어진 조건을 놓침 : f1 = 1, f2 = 2 부터 시작한다는 점을 놓쳐 f1 = 0, f2 = 1로 잡았음
# 2. 지속적으로 실패한 원인 : while문의 시작부분에 n, m = m, n + m으로 바로 계산을 해주는 바람에
# 1 100인 경우 시작지점인 1을 놓치고 바로 계산하여 2부터 카운트하는 오류가 있었음
def fibo(a, b):
    n, m, count = 1, 2, 0  # 처음 오답 원인, 문제에 주어진 1부터 시작한다는 말을 놓침
    while True:  # 계속해서 틀린원인
        # n, m = m, n + m 으로 시작하는 바람에 1 100을 넣으면 시작지점인 1을 놓치고 2부터 카운트, 최종적으로 1이 부족했음
        if n > b:
            print(count)
            break
        if n >= a:
            count += 1
        n, m = m, n + m
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    fibo(a, b)