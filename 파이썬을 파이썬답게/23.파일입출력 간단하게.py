# 다른 언어의 경우
"""
f = open("myfile.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    raw = line.split()
    print(raw)
f.close()
"""
# 파이썬의 경우
with open("myfile.txt") as file:
    for line in file.readline():
        print(line.strip().split("\t"))
