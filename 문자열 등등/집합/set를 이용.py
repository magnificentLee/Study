"""
a = set()
a = set([i for i in range(1, 11])
a.add(n)  : 원소 n 추가
a.remove(n) : 원소 n 제거, 만약 n이 존재하지 않을 경우 런타임에러(keyerror)가 발생함
a.discard(n) : 원소 n 제거, 존재하지 않을 경우에도 정상적으로 작동함
"""
# 아래 코드는 keyerror = 11 을 출력하는 코드
"""
a = set(i for i in range(1, 11))
a.remove(11)
print(a)
"""