# 값의 갯수, 범위가 매우 크기 때문에 일반적인 정렬로는 안 될 것 같음
# 다만 문제의 난이도를 고려하면 정렬을 써도 될 것 같음
n = int(input())
a = sorted(map(int, input().split()))
tmp = 1
for i in a:
    if i > tmp or tmp > i:
        break
    else:
        tmp += 1
print(tmp)