python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n") #
print(index)
index = python.index("n", index + 1) # 5 + 1 번째 위치부터 n 찾기
print(index)

print(python.find("n"))
print(python.find("Java")) # 없을 경우 -1