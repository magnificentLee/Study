"""t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a + b)"""
t = int(input())
c_list = []
for i in range(t):
    a, b = map(int, input().split())
    c_list.append(a + b)
print(int(c_list), sep="\n")
