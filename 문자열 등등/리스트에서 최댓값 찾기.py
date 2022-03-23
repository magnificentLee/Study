# 백준 16401번을 풀던중 테스트한 내용
# 이미 정렬된 값을 리스트에 넣어줄 때 리스트의 최댓값을 이용해야 할 때
# max(li)와 li[-1] 을 이용하는 것 중에 어떤 방법이 더 빠른지를 테스트해봄
import time
start = time.time()
li = [i for i in range(1, 100000001)]
print(li[-1])
end = time.time()
print(end - start)
# 1~10억 까지의 리스트를 만들때
# max(li)는 5.69초가 걸림
# li[-1]은 4.72초가 걸림
# 이미 정렬된 리스트에선 인덱스를 이용하는 방법이 가장 빠른 것 같음
