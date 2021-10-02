t = int(input())
count = zero_count = 0
for i in range(t):
    a = int(input())
    if a == 1:
        count += 1
    else:
        zero_count += 1
if count > zero_count:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
