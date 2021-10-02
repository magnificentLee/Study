# 55-50+40

n = input().split("-")
val_list = []
for i in n:
    m = i.split("+")
    val = 0
    for j in m:
        val += int(j)
    val_list.append(val)
n = val_list[0]
for i in val_list[1:]:
    n -= i
print(n)
