n = int(input())
num = 1

while n > num:
    n -= num
    num += 1
if num % 2 != 0:
    up = num - n + 1
    down = n
else:
    up = n
    down = num - n + 1
print("{}/{}".format(up, down))