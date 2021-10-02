from sys import stdin

n, m, k = map(int, stdin.readline().split())

data = sorted(map(int, stdin.readline().split()), reverse=True)

data_max = data[0]
data_max_2nd = data[1]

count = m // (k + 1) * k
count += m % (k + 1)

result = 0
result += count * data_max
result += (m - count) * data_max_2nd

print(result)