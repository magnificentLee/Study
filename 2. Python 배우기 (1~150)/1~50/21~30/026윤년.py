# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
y = int(input())

# if y % 4 == 0 or y % 400 == 0 and y % 100 != 0: # 1900년도 1로 나옴
# and, or 중에 and의 우선순위가 높기 때문
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("1")
else:
    print("0")
""" 간략도
2012 - T and T = T, T or F = T
1900 - T and F = F, F or F = F
2000 - T and T = T, T or T = T
and 와 or의 진행에 대해서 주의할것.
"""