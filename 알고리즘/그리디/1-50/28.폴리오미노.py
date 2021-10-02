# 처음 생각한 방법
# . 을 기준으로 나눠서 for i in n: 형식으로 돌려서
# 만약 len(i) % 2 == 1 일 때 -1을 출력하는 방식
# 하지만 더 쉽고 간편한 방법이 있음
n = input()
n = n.replace("XXXX", "AAAA")
n = n.replace("XX", "BB")
if "X" in n:
    print(-1)
else:
    print(n)