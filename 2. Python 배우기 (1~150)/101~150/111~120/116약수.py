# 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고,
# 2보다 크거나 같은 자연수이고, 중복되지 않는다.
# 첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
"""
Input
2
4 2
Output
8
"""
# 12 = 2 4 6, 24 = 2 4 6 8 12 즉, i[0] * i[n]
num = int(input())
num_list = sorted(map(int, input().split()))
n = num_list[0] * num_list[num - 1]
print(n)
