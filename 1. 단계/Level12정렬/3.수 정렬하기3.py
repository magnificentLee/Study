# 메모리 초과
"""
import sys

t = int(input())
n = []
for _ in range(t):
    n.append(int(sys.stdin.readline()))
for i in sorted(n):
    print(i)
"""
# 할당된 메모리가 적기 때문에 input을 처음에 다 받아서 저장하면 무조건 시간 초과가 뜬다.
# 따라서 10000이 들어갈 수 있는 리스트를 미리 만들어 준 뒤 하나씩 더해주고 메모리에서 없애버리는
# 방식을 사용해야 한다.
# 팁
# 1. input() 대신 sys.stdin.readline() 을 사용할 것
# 2. for 문에서 range() 안에 sys.stdin.readline() 을 넣지 말고 int(sys.stdin.readline())
# 으로 따로 뺄 것(이것 하나로 성패가 갈림)
# 3. for문에서도 i가 필요 없는 부분은 _ 로 처리할 것
import sys

t = int(input())
count = [0 for _ in range(10001)]  # [0] * 10000
for _ in range(t):
    # 중복되는 숫자가 있을 경우 2 이상의 값이, 아니면 1, 없으면 0
    count[int(sys.stdin.readline()) - 1] += 1
for i in range(10001):
    # idx 0 = 1
    # count 0 = 2 일 경우 1 을 두 번 출력
    [print(i + 1) for _ in range(count[i])]
