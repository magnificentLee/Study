t = int(input())
n = []
for _ in range(t):
    word = input()
    word_length = len(word)
    n.append((word, word_length))
n = list(set(n))
n.sort(key=lambda x: (x[1], x[0]))  # 우선순위 1.길이 2.알파벳
for i in n:
    print(i[0])
