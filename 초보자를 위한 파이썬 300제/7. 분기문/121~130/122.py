"""
score = int(input("score: "))
if score >= 81:
    print("grade is A")
elif score >= 61:
    print("grade is B")
elif score >= 41:
    print("grade is C")
elif score >= 21:
    print("grade is D")
else:
    print("grade is E")
"""
score = input("score: ")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")