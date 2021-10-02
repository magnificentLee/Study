""" 1차 시도
a = int(input())
if a%4 == 0 and a%100 != 0:
    print('1')
elif a%100 == 0 and a%400 !=0:
    print('0')
elif a%400 == 0:
    print('1')
else:
    print('0')
"""
""" 2차 시도
a = int(input())
if a%4 == 0 and a%100 != 0 or a%400 == 0:
    print(1)
else:
    print(0)
2차 시도는 제일 짧은 코드를 사용한 것으로 조건을 한 곳에 몰아 넣은 방식임
print에 정수형, 문자형 구분할 필요 없음
"""