# 문제는 팰린드롬으로 보임
# 이해하는데 좀 걸렸음
# 비밀번호들이 주어질때 a = 비밀번호중 하나, b = a를 뒤집은 것, a == b 라면 a 가 정답
# a != b 라면 a를 뒤집은게 비밀번호 목록에 있다면 정답, 없다면 다음 비밀번호를 확인
# 간결한 코드를 위해 a 를 리스트에 확인하게끔 수정

t = int(input())
code = [input() for _ in range(t)]
for i in code:
    if i[::-1] in code:
        l = len(i)
        print(l, i[l // 2])
        break