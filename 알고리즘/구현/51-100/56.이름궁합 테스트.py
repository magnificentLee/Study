alp = {"A": 3, "B": 2, "C": 1, "D": 2, "E": 4, "F": 3, "G": 1, "H": 3, "I": 1, "J": 1, "K": 3,
       "L": 1, "M": 3, "N": 2, "O": 1, "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2, "U": 1, "V": 1,
       "W": 1, "X": 2, "Y": 2, "Z": 1}
n, m = map(int, input().split())  # 이름 길이들
a, b = input().split()
l = n + m
tmp = []
if n >= m:
    for i in range(m):
        tmp.append(a[i])
        tmp.append(b[i])
    for i in range(m, n):
        tmp.append(a[i])
else:
    for i in range(n):
        tmp.append(a[i])
        tmp.append(b[i])
    for i in range(n, m):
        tmp.append(b[i])
for i in range(l):
    tmp[i] = alp[tmp[i]]
# len(tmp) == 22일때 20번 수행하므로 for i in range(22 - 2)
# 매 수행마다 전체길이가 1씩 감소하며 최종적으로 2개가 남음
# 22개의 숫자를 각 횟수마다 21 - (1 :계속증가) 회 시행, 최종적으로 리스트의 idx:0, 1 이 결론
# 계산 결과 1951402, 2013347 이 나오는데 10으로 나눈 나머지를 합치면 될 것 같음
for i in range(l - 2):
    for j in range(l - 1 - i):
        tmp[j] += tmp[j + 1]
# str로 합칠 경우 0 + 1 = 01% 가 되기 때문에 방법을 바꿈
result = (tmp[0] % 10) * 10 + tmp[1] % 10
print("%s%%" % result)
# print("{}%".format(result)) 로 해도 됨
