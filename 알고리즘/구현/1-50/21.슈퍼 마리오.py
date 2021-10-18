n = [int(input()) for _ in range(10)]
result = 0
for i in range(10):
    result += n[i]
    if result == 100:
        break
    elif result > 100:
        before = sum(n[:i]) # 이전까지의 합
        if abs(result - 100) > abs(100 - before):
            result = before
            break
        else:
            break
print(result)