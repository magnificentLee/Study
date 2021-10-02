line = "The general pattern to count the words in a line of text"

words = line.split()
print("Words:", end=" ")
print(*words, sep=", ")

# print("Words:", *words, sep=", ") 로 할 경우
# Words:, The, general, pattern, to, count, the, words, in, a, line, of, text
# 라는 결과가 나오기 때문