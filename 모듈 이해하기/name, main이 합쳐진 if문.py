# 18111번 마인크래프트 문제를 풀던중 발견한 방법으로 아마 파이썬으로 풀리는 유일한 방법일 것임
# https://5w33th0me4jisu.tistory.com/ 출처
# 기존의 방법 : 파이파이3으로 125344KB 860ms
# 새로운 방법 : 파이썬3 으로  33648KB 164ms
# 이해가 안 가던 구문
"""
from sys import stdin
input = stdin.readline
if __name__ == "__main__":
    n, m, b = map(int, input().split())
    grounds = []
    for _ in range(n):
        grounds.extend(list(map(int, input().split())))
만약 input = stdin.readline() 으로 바꿀 경우
if __name__ 밑으로 input 뒤의 "()" : call 부호를 다 지워야 됨
"""
"""
if __name__ == "__main__":
    코드
"""
"""
# taengModule.py 라는 파일을 만들고 아래를 입력해주고
def add(x, y):
    return x + y
다른 파일에서 모듈을 불러와서 실행해본다
import taengModule
print(taengModule.add(2, 3))
결과 = 5
"""
"""
# taengModule.py 를 수정
def add(x, y):
    return x + y
print(add(3, 4))
다른 파일에서 모듈을 불러오면
import taengModule
결과 = 7
"""
"""
taengModule 의 add 함수만을 사용하기 위해선(즉, print 기능을 제외한)
taengModule의 코드를 수정해줘야 한다
def add(x, y):
    return x + y
if __name__ == "__main__":
    print(add(3, 4))
"""
import taengModule
print(taengModule.add(3, 4))
# 결과 = 7
# 반대로 taengModule 파일을 직접 실행해도 결과가 7 이 나온다
# 요컨대 직접 파일을 실행하는 경우에 한해서 작동하게 만든다는 것