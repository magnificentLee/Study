t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(2 - a + b)  # 면의 수 = 2 - 꼭짓점의 수 + 모서리의 수
