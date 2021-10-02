n = int(input())
m = list(map(int, input().split()))
m_max = max(m)
for i in range(n):
    m[i] = m[i] / m_max * 100
avg = sum(m) / n
print("%.2f"%avg)
