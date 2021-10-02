import sys

data = sys.stdin.readline().rstrip()

print(data)
"""
rstrip() 을 넣지 않을 경우 엔터가 줄 바꿈 기호로 입력됨
일례로 Hello World! 를 입력할 경우 
출력값인 Hellow World! 와 실행 종료 문구인
Process finished with exit code 0 사이에 빈공간이 두 개가 생긴다
일반적인경우 한 개만 나와야 됨
"""