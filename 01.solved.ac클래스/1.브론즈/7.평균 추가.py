t = int(input())
n = sorted(map(int, input().split()), reverse=True)
result = [(i/n[0])*100 for i in n]
print("%.2f"%(sum(result)/t))
# 문제가 리스트 모든 요소를 바꾼다는 점에 주의, 최댓값이라도 예외 없음