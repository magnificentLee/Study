# 백준 11104 Fridge of Your Dreams
# 2 진수를 10 진수로 바꾸는 법
# 1. a = 문자열, int(a, 2)
# 2. int(0b2진수)
# 2번의 경우 해당 케이스에 적용하기 어렵기 때문에 1번으로 진행
# 1번
print(int(0b000000000001010101010101))
# Output : 5461

# 2번
"""
for _ in range(int(input())):
    n = input()
    print(int(n, 2))
"""