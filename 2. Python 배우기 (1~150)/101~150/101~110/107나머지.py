import sys

n_list = []
for i in range(10):
    n = int(sys.stdin.readline())
    n = n % 42
    if n in n_list:
        pass
    else:
        n_list.append(n)
print(len(n_list))
