"""a = int(input())
b = int(input())

print(a * (b % 10))
print(a * ((b % 100) // 10))
print(a * (b // 100))
print(a * b)"""
a = int(input())
b = int(input())
print(a * (b % 10), a * ((b // 10) % 10), a * (b // 100), a * b, sep="\n")
