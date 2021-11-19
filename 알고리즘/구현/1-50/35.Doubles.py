# 리스트를 정렬, 시작값을 시작값다음~리스트끝까지 확인하여 2배 값이 존재하면 결과+1
while True:
    n = sorted(map(int, input().split()))
    result = 0
    if -1 in n:
        break
    for i in range(len(n) - 1):
        if n[i] * 2 in n[i + 1:]:
            result += 1
    print(result)