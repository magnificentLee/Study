# 원형 유지를 못하는 경우
compare = list("dog")
compare_word = compare
compare.pop(0)
print(compare)
print(compare_word)

# 원형 유지를 하는 경우
compare2 = list("dog")
compare2_word = compare2[:]
compare2.pop(0)
print(compare2)
print(compare2_word)
