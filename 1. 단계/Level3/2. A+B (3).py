"""
처음 테스트 케이스의 개수를 입력
그 다음 A와 B가 주어짐
"""
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a + b)