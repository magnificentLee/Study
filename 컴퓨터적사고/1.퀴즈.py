# 깜짝 퀴즈) 다음 코드를 실행하면 출력값이 어떻게 될까요?

def three():
    print("three", end=" ")
    return 3


def five():
    print("five", end=" ")
    return 5


def seven():
    print("seven", end=" ")
    return 7


# main code
three() > five() > seven()

"""
일단 함수가 호출되고 실행되는 절차를 생각해보면

1. 함수호출
2. 출력
3. 리턴

위와 같은 순서로 진행이 될겁니다.

그렇게 따지면 일단 가장 처음에 
three함수 호출 -> three 출력 -> 3 리턴
-> 비교 시작 -> five 함수 호출 -> five 출력 -> 5 리턴 -> 비교 완료 false 리턴 -> 종료

따라서 three와 five만 출력
"""