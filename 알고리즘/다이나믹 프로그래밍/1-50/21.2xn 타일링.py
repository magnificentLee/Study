# 직접 그려가면서 규칙을 찾은 결과
# n = 1, 2, 3, 4, 5 ... (순서)
# m = 1, 2, 3, 5, 8 ... (count)
# 즉, 피보나치 수열임
# 일반적인 피보와 다른점은 10이 아닌 9일때 55 라는점
# 오답이 나오는 이유가 10007로 나눈 나머지를 출력하라는 점을 깜빡했기 때문임
n = int(input())


def fibo(m):
    a, b = 0, 1

    for i in range(m):
        a, b = b, a + b
    return b


print(fibo(n) % 10007)


# 다른 사람 코드중 신기했던 코드
# 내용은 엄청 단순한데 속도가 68ms(내 코드는 80ms)로 훨씬 빨랐음
"""
n= int(input())
dp=[0]*(n+1)

if n==1:
  dp[1]=1
elif n==2:
  dp[1]=1
  dp[2]=2
else:
  dp[1]=1
  dp[2]=2
  for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%10007

print(dp[n])
"""
# 다른 코드2
# 피보나치의 경우 dp보다 치환을 이용하는게 훨씬 빨랐기 때문에 치환을 사용했지만
# 해당 코드는 dp, append를 이용함에도 68ms의 속도가 나왔음
"""
a = int(input())
b = list()
b.append(1)
b.append(2)
for i in range(2,a):
    b.append(b[i-1] + b[i-2])
print(b[a-1]%10007)
"""