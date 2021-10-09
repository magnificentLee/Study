from sys import stdin
input = stdin.readline

t = int(input())
n = sorted([int(input()) for _ in range(t)])
print(*n, sep="\n")
