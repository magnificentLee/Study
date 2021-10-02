greet = "Hello Bob"
greet_small = "hello bob"
print(greet.lower())  # hello bob
print(greet.upper())  # HELLO BOB
print(greet_small.capitalize())  # Hello bob
result = ""
for i in greet_small.split():
    result += i.capitalize()
    result += " "
print(result.rstrip())  # Hello Bob
