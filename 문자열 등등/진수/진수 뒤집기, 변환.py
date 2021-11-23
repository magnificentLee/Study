# 11179번 2진수 뒤집기 문제
# 파이썬엔 진수 변환 내장 함수를 제공함
# 정확히는 진수 형태의 문자열로 변환해줌
# bin, oct, str, hex : 2, 8, 10, 16
# bin(42) : 0b101010 : (0b제외)101010 = 2진수42
# oct(42) : 0o52     : (0p제외)52     = 2진수42
# hex(42) : 0x2a     : (0x제외)2a     = 2진수42
# int(a, b) : a = 변환하고 싶은 변수(문자), b = 변환하고 싶은 진수
# ex) 2진수 "0b1101" 을 10진수로 변환하고 싶으면 print(int("0b1101", 2)) 를 사용하면 됨
n = int(input())
bin_n = bin(n).split("0b")[1]
n_re = [i for i in reversed(bin_n)]
tmp = "0b"
for i in n_re:
    tmp += i
result = int(tmp, 2)
print(result)