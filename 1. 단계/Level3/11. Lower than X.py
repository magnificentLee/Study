n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if x > a[i]:
        print(a[i], end= " ")
""" 
for, if 동시 사용, map으로 list를 감싸기
end ="" : 문장을 출력하고 마지막에 무엇을 쓰고 끝낼지 정할 때 사용, 없으면 1행으로 나옴
"""