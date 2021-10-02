# 단순히 최댓값 - 기준값이 아님 만약 5 7 7 7 일 경우 7 - 5 = 2가 아닌 3임
# 반례에 주의할 것
# 후보가 1명인 경우, 처음부터 최댓값이 다솜이인 경우
from sys import stdin as st

n = int(st.readline())
das = int(st.readline())
# others를 입력과 동시에 정렬하려고 하면 런타임에러가 발생함
# 아마 n = 1인경우 입력 받을 값이 없기 때문에 발생하는 것 같음(백준에서만)
# 따라서 if 문을 통과한 경우부터 정렬하게끔 수정했음
others = [int(st.readline()) for _ in range(n - 1)] # candidates
count = 0
if n > 1: # n != 1 인 경우도 통과됨
    others.sort(reverse=True)
    while das <= others[0]:
        das += 1
        others[0] -= 1
        count += 1
        others.sort(reverse=True)
    print(count)
else:
    print(0)