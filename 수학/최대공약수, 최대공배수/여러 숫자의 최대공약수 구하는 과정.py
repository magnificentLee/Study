def gcd(a, b):
    while b != 0:
        res = a % b
        a = b
        b = res
    gcd = a
    return gcd

#array = [6, 9, 12, 18]  # min(gcd_list) = 3 : 최대공약수
array = [1, 2, 4, 8]  # min(gcd_list) = 1 : 최대공약수
gcd_list = []
for i in range(len(array)):
    for j in range(i, len(array)):
        gcd_list.append(gcd(array[i], array[j]))
print(set(gcd_list))
print(gcd(6, 9))