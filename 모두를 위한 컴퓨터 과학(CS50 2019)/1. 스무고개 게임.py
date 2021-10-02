"""
1) 친구와 1부터 100까지 숫자 중 1가지 숫자를 맞추는 스무고개 게임을 하려고 합니다.
이 때 사용할 알고리즘을 의사코드로 표현하면 어떻게 될까요?
1. 게임을 제안한다.
2. 거절하면 종료, 수락하면 게임 시작.
3. 문제 출제자가 1~100 중 랜덤한 숫자(result)를 생각한다.
4. 게임 진행자가 1~100 중 랜덤한 숫자(n)를 말한다.
5. 시행횟수가 20번을 초과하지 않는 동안 아래 과정(7~9)을 반복.
6. 만약 result == n 이면 게임 진행자의 승리, 반복문 탈출.
7. 만약 result > n 이면 result > n 이라고 말해준다.
8. 만약 result < n 이면 result < n 이라고 말해준다.
9. 만약 위 과정에서 정답이 나오지 않을 경우 문제 출제자의 승리, 정답을 말해준다.
10. 게임 종료
"""
# 이하는 개인적으로 구현한 게임
import random
print("스무고개 하자")
friend = input()
if "하자" not in friend:
    pass
else:
    result = random.randrange(1, 101)
    t = 1
    b = False
    while t <= 20:
        n = int(input())
        if result == n:
            b = True
            break
        elif result > n:
            print("result > n")
        else:
            print("result < n")
        t += 1
    print("정답은:", result)
    if b is True:
        print("게임 진행자의 승리")
    else:
        print("문제 출제자의 승리")
print("게임 종료")