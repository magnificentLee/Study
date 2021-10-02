import sys

t = int(sys.stdin.readline())
count = 0
first = 666
while True:
    if "666" in str(first):
        count += 1
    if t == count:
        print(first)
        break
    first += 1