# 1. 11053 가장 긴 증가하는 부분 수열
# 2. 11722 가장 긴 감소하는 부분 수열
n = 6  # 기존 : int(input()), 리스트의 길이
array_up = [10, 20, 10, 30, 20, 50]  # 증가 리스트, 기존 : list(map(int, input().split()))
array_down = [10, 30, 10, 20, 20, 10]  # 감소 리스트, 기존 : list(map(int, input().split()))
dp_up = [1] * n  # 증가 수열 확인용, 시작 값을 포함하기 때문에 1을 넣어줌
dp_down = [1] * n  # 감소 수열 확인용, 시작 값을 포함하기 때문에 1을 넣어줌
# 두 문제는 if문에서 달라지기 때문에 같은 반복문을 활용
for i in range(1, n):
    for j in range(i):
        if array_up[j] < array_up[i]:  # 증가용 if문
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)
        if array_down[j] > array_down[i]:  # 감소용 if문
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)
print("가장 긴 증가하는 부분 수열 %i" % max(dp_up))  # 정답 : 4
print("가장 긴 감소하는 부분 수열 %i" % max(dp_down))  # 정답 : 3
