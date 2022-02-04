# 메모이제이션의 절반 정도의 시간밖에 안 걸림
import time
start = time.time()
# 피보나치 시작
def fibo(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a
print(fibo(int(input())))
# 피보나치 끝
end = time.time()
print(end - start)
