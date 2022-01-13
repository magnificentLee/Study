n = input()
l = len(n)
result = []
for i in range(l - 2):
    for j in range(i + 1, l - 1):  # 중간 나누는 부분
        for k in range(j + 1, l):
            tmp = n[:j][::-1] + n[j:k][::-1] + n[k:][::-1]
            result.append(tmp)
print(min(result))