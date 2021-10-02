""" 1차 시도
a = input()
b = input()
li2 = list(b)
out1 = int(a)*int(li2[2])
out2 = int(a)*int(li2[1])
out3 = int(a)*int(li2[0])
out4 = int(a)*int(b)
print(out1, out2, out3, out4, sep = "\n")
"""
""" 2차 시도
a = input()
b = input()
li2 = list(b)
print(int(a)*int(li2[2]), int(a)*int(li2[1]), int(a)*int(li2[0]), int(a)*int(b), sep = "\n")
"""
a, b = int(input()),int(input())
print(a*(b%10), a*((b%100)//10), a*(b//100), a*b, sep = "\n")
"""
3차 시도는 나머지(%)과 몫(//)를 이용
b % 10 = 5
b % 100 = 85 /와 10의 몫 = 8
b // 100 = 3 
각각의 결과를 a와 곱하면 결과가 나옴
"""