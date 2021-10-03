n = int(input())

atm = sorted(map(int, input().split()))
result = 0
tmp = 0
for i in atm:
    tmp += i
    result += tmp
print(result)