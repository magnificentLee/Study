from sys import stdin as st
t = int(st.readline())
for _ in range(t):
    n = int(st.readline())
    # 시험결과 순으로 정렬
    cand = sorted([list(map(int, st.readline().split())) for _ in range(n)], key=lambda x: x[0])  # candidates
    # 람다식의 유무로 약 2,000 ms 의 시간 차이가 발생함
    result = 1  # 첫번째 기준은 무조건 포함되기 때문
    cand_min = cand[0][1]  # 기준, 면접결과로 비교
    for i in range(1, n):
        if cand[i][1] < cand_min:
            cand_min = cand[i][1]
            result += 1
    print(result)
""" 첫번째 시험성적을 기준으로 정렬
1 4  기준값 count
2 5  no count
3 6  no count
4 2  min = 2, count
5 7  no count
6 1  min = 1, count
7 3  no count
"""


