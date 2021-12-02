n = list(input().split())
start = n[0]
end = n[1:]
array = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
result = ""
result += start[0].capitalize()
for i in range(len(end)):
    if end[i] in array:
        continue
    else:
        result += end[i][0].capitalize()
print(result)