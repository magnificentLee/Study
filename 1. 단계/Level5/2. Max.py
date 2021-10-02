a = []
for i in range(9):
    a.append(int(input()))

print(max(a))
print(a.index(max(a)) + 1)  # -1만큼 나오기 때문