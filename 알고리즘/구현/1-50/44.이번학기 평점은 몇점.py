# 꼼수 : 소주 2번째에서 반올림을 해주는 것을 이용 소수 3번째 자리에 1을 더해주면 round 함수의 오류를 커버 가능
# 즉, 0.001 을 더해주면 부동소수점을 이용하는 round 함수의 오류를 해결 가능, but 문제 의도는 이게 아닐것
# 직접 반올림 함수를 구현하는 것을 목표로 하는 것 같음
def rnd(n):
    n *= 1000
    if n % 10 >= 5:
        n += 10
        n -= n % 10
    n /= 1000
    return n
# return f"n:.2f"  # 새로 배운 방법, 제일 밑 print를 간소화 가능

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D+", "D0", "D-", "F"]
points = [4.3, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
up, down = 0, 0
for _ in range(int(input())):
    string = input().split()
    up += int(string[1]) * points[grades.index(string[2])]
    down += int(string[1])
total = up / down
result = rnd(total)
print("%0.2f" % result)


# %0.2f 가 없을 경우 결과
"""
7
General_Physics_1 3 A+
Introduction_to_Computer_Science_and_Eng 3 B0
Reading_And_Writing 2 C0
English_1 3 C+
ASS 2 C-
BSS 3 C-
CSS 2 B0
OUPUT
2.635555555555556
"""
# 오답 발생 코드 : 테스트 결과 해당부분이 문제가 맞음
# 단순히 더해버리기만 하면 모종의 테스트 결과에서 소숫점 3번째 밑으로 남는 결과가 생기는것 같음
"""
def rnd(n):
    n *= 1000
    if n % 10 >= 5:
        n += n % 10
    n /= 1000
    return n
"""
"""
def rnd(n):
    n *= 1000
    if n % 10 >= 5:
        n += 10
        n -= n % 10
    n /= 1000
    return f"n:.2f"  # 새로 배운 방법
"""