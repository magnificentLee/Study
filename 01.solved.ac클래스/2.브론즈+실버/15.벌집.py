# 1 / 7 / 19 / 37
#  +6  +12  +18
n = int(input())
start = 1
inc_num = 6
count = 1
while n > start:
    count += 1
    start += inc_num
    inc_num += 6
print(count)
