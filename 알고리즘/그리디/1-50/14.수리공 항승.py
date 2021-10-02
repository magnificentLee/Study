"""
n, l = map(int, input().split())

pipe = list(map(int, input().split()))
pipe.sort()

start = 0
count = 0
for broke in pipe:
    if start < broke:
        start = broke + l - 1
        count += 1
print(count)
"""
n, l = map(int, input().split())

pipe = list(map(int, input().split()))
pipe.sort()
start = pipe[0]
end = pipe[0] + l
result = 1
for i in range(n):
    if start <= pipe[i] < end:  # end 값을 포함하지 않았기 때문에 l - 1을 할 필요가 없다
        continue
    else:
        start = pipe[i]
        end = pipe[i] + l
        result += 1
print(result)