""" 기존
string = "X-DSPAM-Confidence: 0.8475"

head = string.find(":")
tail = string[head + 2:]
value = float(tail)
print(value)
"""
string = "X-DSPAM-Confidence: 0.8475"

number = string.split()[1]
result = float(number)
print(result)
