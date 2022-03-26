# 백준 1166 선물
# 길이, 너비, 높이에서 최댓값을 end로 잡자

n, l, w, h = map(int, input().split())
start, end = 0, max(l, w, h)
for _ in range(10000):
    mid = (start + end) / 2
    result = (l // mid) * (w // mid) * (h // mid)
    if result >= n:
        start = mid
    else:
        end = mid
print("%.10f" % end)