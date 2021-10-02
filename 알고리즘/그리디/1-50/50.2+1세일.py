from sys import stdin as st

def milks(array, n):
    k = 2
    result = 0
    for i in range(n):
        if i == k:
            k += 3
            continue
        result += array[i]
    return result


n = int(st.readline())
milk = sorted([int(st.readline()) for i in range(n)], reverse=True)
print(milks(milk, n))