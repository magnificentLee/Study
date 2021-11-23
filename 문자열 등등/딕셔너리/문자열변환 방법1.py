data = {"a": "A", "A": "a"}

string = input()
result = ""
for i in string:
    result += data[i]
print(result)
"""
Input
aaaAaaa
Output
AAAaAAA
"""