# 처음 이해했던게 맞는것 같다
# 중간에 질문검색에서 봤던 bbanaana bana = 2 의 경우
# b + bana + a + n + a = 5 가 나오는 것으로 보아 중간에 추가하는 건 안 되는 것 같음
# 거의 동일한 문제
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_65wkqsb4DFAWS&categoryId=AV_65wkqsb4DFAWS&categoryType=CODE
# https://mungto.tistory.com/241
# 처음 생각했던 방식
# 정답 = 부분카운트 + 전체길이 - (부분길이 * 부분카운트)
for _ in range(int(input())):
    s, p = input().split()
    n, m = len(s), len(p)
    c = s.count(p)
    res = c + n - (m * c)
    print(res)

# 아래는 다른 사람이 삼성SW에서 유사한 문제를 풀었던 방법
"""
for _ in range(int(input())):
    a, b = input().split()
    print(f'{len(a)-(len(b)-1)*a.count(b)}')
"""