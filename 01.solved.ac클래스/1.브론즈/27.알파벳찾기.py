"""
n = list(input())
alpha = list("abcdefghijklmnopqrstuvwxyz")
arr = [-1 for i in range(26)]
for i in range(len(n)):
    for j in range(len(alpha)):
        if alpha[j] in n:
            idx = n.index(alpha[j])
            arr[j] = idx
for i in arr:
    print(i, end=" ")
"""
# 짧게, find 함수-없을 경우 -1 반환하는 점에서 작성
n = input()
alpha = list(range(97, 123))
for i in alpha:
    print(n.find(chr(i)), end=" ")