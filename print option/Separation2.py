#S,E,P 대신 계산 결과를 넣고 @ 대신 \n 을 넣는 식으로 print 사용을 줄일 수 있다의 예제
a, b = input("a, b 값을 입력하시오").split()
a = int(a)
b = int(b)
print(a+b, a-b, a*b, int(a/b), a%b, sep = '\n')
#int(a/b)는 계산 결과 소숫점 버림