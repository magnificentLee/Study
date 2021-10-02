# 아스키코드를 이용하는 방법 ord : 문자 to 숫자
# a : 97 이므로 96을 빼주면 1이 될 것
t = int(input())
n = input()
result = 0
for i in range(len(n)):
    dot = ord(n[i]) - 96
    result += dot * (31 ** i)
print(result % 1234567891)
