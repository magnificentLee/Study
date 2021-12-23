# 단순 브루트포스 문제?
n = input()
l = len(n)
result = []
for i in range(l - 2):
    for j in range(i + 1, l - 1):  # i + 1 을 안 해줬기 때문에 중간에 중복되는 경우가 있었나봄
        for k in range(j + 1, l):  # j + 1 마찬가지, 그래서 오답 발생
            word = n[:j][::-1] + n[j:k][::-1] + n[k:][::-1]
            result.append(word)
print(min(result))