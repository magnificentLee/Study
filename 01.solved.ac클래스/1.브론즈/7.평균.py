t = int(input())
n = list(map(int, input().split()))
n_list = []
n_max = max(n)
for i in n:
    n_list.append((i / n_max) * 100)
print("%.2f"%(sum(n_list) / t))