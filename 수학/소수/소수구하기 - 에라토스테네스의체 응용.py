# 1929번 문제 : 에라토스테네스의 체를 이용한 방법
# 240ms, 350B, 38732KB
# 기존 방법은 3964ms, 286B, 28776KB 로 메모리만 제외하면 제일 빠른 방법임
def prime(start, num):
    p = [True] * num
    for i in range(0, 2):
        p[i] = False
    for i in range(2, int(num ** 0.5) + 1):  # 2~제곱근까지만 확인해도 소수 판별 가능
        if p[i]:
            for j in range(i + i, num, i):  # i 이후 i 의 배수들을 False 판정
                p[j] = False
    return [i for i in range(start, num) if p[i] == True]
#  return 값에 num + 1 을 할 경우 인덱스 오류가 나기 때문에 주의할것


m, n = map(int, input().split())  # sys.stdin.realine : 속도 변화 없음
print(*prime(m, n + 1), sep="\n")  # m 이상 n 이하 이므로 n 까지 포함

# 반례 n이 소수인 경우를 포함해보면 바로 알 수 있음