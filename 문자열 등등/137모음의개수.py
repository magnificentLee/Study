lang = list(input())
alpha = "aeiou"
count = 0
for i in lang:
    if i in alpha:
        count += 1
print(count)