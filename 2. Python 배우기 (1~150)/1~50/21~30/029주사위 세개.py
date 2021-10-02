# 제일 간단하고 알아보기 쉬운 방법임!
a, b, c = map(int, input().split())

# total = [a, b, c] 수정전

if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100) # 수정후
    # print(max(total) * 100) 수정전

# 굳이 리스트를 사용하지 않아도 된다
# max(a, b, c) 로 해줘도 된다!
