# 내풀이
n, d = input().split()
result = 0
for i in range(1, int(n) + 1):
    result += str(i).count(d)
print(result)

# 숏코딩 + 최단시간
"""
a,b=map(int,input().split())
print(''.join(map(str,range(1,a+1))).count(str(b)))
"""