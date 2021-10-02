t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))
# Insert Sort : 삽입정렬
for i in range(1, len(n)):  # t 혹은 len(n)
    while (i > 0) & (n[i] < n[i - 1]):
        n[i], n[i - 1] = n[i - 1], n[i]

        i -= 1
for j in n:
    print(j)
