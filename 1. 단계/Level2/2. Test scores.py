""" 1차 시도
a = int(input())
if 90 <= a <= 100: print('A')
elif 80<= a <= 89: print('B')
elif 70<= a <= 79: print('C')
elif 60<= a <= 69: print('D')
else: print('F')
"""
a=int(input())
if a>=90: print('A')
elif a>=80: print('B')
elif a>=70: print('C')
elif a>=60: print('D')
else: print('F')
"""
길이가 제일 짧은 코드, 
자세하게 범위를 지정해주지 않아도 앞의 if에 있는 범위를 사용하는 방식임  
"""