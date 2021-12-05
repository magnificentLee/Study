# 어떤 지점까지 증가하다 감소하는 것 감소하다 중간에 증가하는 것 : X
# 계속 증가하는 것 : O
# 동일한 높이가 있는 것 : X
n = int(input())
a = list(map(int, input().split()))
flag, height = 1, 1  # 정답 판별 값, 높이는 기본적으로 증가한다고 가정
for i in range(1, n):
    if a[i - 1] == a[i]:
        flag = 0
        break
    else:  # 증가 혹은 감소 판별
        if height == 1:
            if a[i - 1] > a[i]:  # 증가하다 감소하게 된다면
                height = 0
        if height == 0:  # 감소하기 시작하면
            if a[i - 1] < a[i]:
                flag = 0
                break
if flag == 1:
    print("YES")
else:
    print("NO")