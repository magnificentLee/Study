# 문제는 접미사 배열이 아님, 접두사 배열을 물어보는 문제임!
# 접두사 : b, ba, ban, bana, banan, banana
# 접미사 : a, na, ana, nana, anana, banana
# 접두사의 배열 순서는 그냥 반복문 순서대로 출력하면 될듯?
a = input()
l = len(a)
for i in range(l, 0, -1):
    print(l - i)