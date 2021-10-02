# count함수 이용
"""
from sys import stdin
input = stdin.readline

document = input().strip()
word = input().strip()
print(document.count(word))
"""

from sys import stdin

doc = stdin.readline().strip()
word = stdin.readline().strip()
l = len(word)
n = 0
result = 0

while n < len(doc):
    if doc[n: n + l] == word:
        result += 1
        n += l
    else:
        n += 1
print(result)

"""
fibo = [0, 1]
for i in range(2, 14):
    f = fibo[i - 2] + fibo[i - 1]
    fibo.append(f)
print(fibo)
"""