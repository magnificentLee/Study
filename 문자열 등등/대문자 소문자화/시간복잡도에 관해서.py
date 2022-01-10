# 대문자화 테스트에 사용될 코드 : 백준 10384
# 테스트 내용
# 문자열을 입력시 대문자화 하는 것과 반복문에서 각각의 문자를 돌 때 즉석해서 대문자화 하는 것중에 어느게 더 빠를까
# n = input().upper() 와 for i in n: idx = ord(str(i).upper()) 에서 시간복잡도를 측정하는것
""" input
1
The quick brown fox jumps over a lazy dog. 을 400번 정도 곱한다고 생각하자(굉자히 긴 문자열이라고 생각)
"""
# 테스트결과
# input().upper() = 0.7476375102996826
# 반복문에서 대문자화 = 0.4443833827972412
# 약 60% 정도 빠름
# 이유는 입력받을때 대문자화 할 경우 반복문을 돌기 때문에 결과적으로 반복문을 두 배로 도는셈이라 그런것 같음

import time
for _ in range(int(input())):
    start = time.time()
    # n = input().upper()
    n = input()
    array = [0] * 26
    for i in n:
        idx = ord(str(i).upper()) - 65
        if 0 <= idx <= 25:
            array[idx] += 1
    end = time.time()
    print(end - start)