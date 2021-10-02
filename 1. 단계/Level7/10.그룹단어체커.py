t = int(input())
count = 0
for i in range(t):
    word = input()
    if list(word) == sorted(word, key=word.find):
        count += 1
print(count)
