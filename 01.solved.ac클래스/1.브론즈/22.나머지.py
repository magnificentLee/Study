re = []
for i in range(10):
    n = int(input())
    re.append(n % 42)
print(len(set(re)))