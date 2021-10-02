num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
if line % 2 == 0:
    top = num
    bottom = line - num + 1
else:
    top = line - num + 1
    bottom = num
print(f"{top}/{bottom}")
# print("{}/{}".format(a, b))
