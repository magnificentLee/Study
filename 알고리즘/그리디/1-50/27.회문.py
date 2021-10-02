from sys import stdin

def secondCheck(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def firstCheck(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            check1 = secondCheck(word, left + 1, right)
            check2 = secondCheck(word, left, right - 1)
            if (check1 or check2):
                return 1
            else:
                return 2
    return 0
n = int(stdin.readline().rstrip("\n"))
for _ in range(n):
    word = stdin.readline().rstrip("\n")  # rstrip 없을 경우 오답출력
    left = 0
    right = len(word) - 1
    result = firstCheck(word, left, right)
    print(result)