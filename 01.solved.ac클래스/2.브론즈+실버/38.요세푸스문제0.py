"""
n, k = 7, 3 기준
1 2 3 4 5 6 7 에서 k:3 = 3의 idx=2
1 2 4 5 6 7 에서 idx2 + 3(k) = 5번째의 idx = 4
1 2 4 5 7 에서 idx4 + 3(k) = 7번째
but len(list) = 5, 7 > 5 이므로 7 % 5 = 2의 idx = 1
1 4 5 7 에서 idx1 + 3(k) = 4번째의 idx = 3
1 4 5 에서 idx3 + 3(k) = 6번째
but len(list) = 3, 6 > 3 이므로 6 % 3 = 0의 idx = 0
but 0번째란 없으므로 0 - 1 = 오른쪽 끝이므로 idx 2 = 3번째
1 4 에서 idx2 + 3(k) = 5, 5 % 2 = 1의 idx= 0
4
다시 없어진 수들을 차례로 리스트에 넣어보면
3, 6, 2, 7, 5, 1, 4
예시로 주어진 결과는 <3, 6, 2, 7, 5, 1, 4>
"""
n, k = map(int, input().split())
num = [i for i in range(1, n + 1)]
i = 0
print("<", end="")  # 시작
while len(num) > 1:
    i = i + k
    if i > len(num):
        i = i % len(num)
        if i == 0:
            i = i + len(num)
    i = i - 1
    print(num.pop(i), end=", ")
print(str(num.pop()) + ">")