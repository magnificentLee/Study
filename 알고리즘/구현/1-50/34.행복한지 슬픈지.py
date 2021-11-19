# 단순히 카운트로 해도 될것
string = input()
h = string.count(":-)")  # happy
s = string.count(":-(")  # sad
if h == 0 and s == 0:
    result = "none"
elif h == s:
    result = "unsure"
elif h > s:
    result = "happy"
else:
    result = "sad"
print(result)