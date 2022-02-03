# 하나의 문자를 더하거나 빼거나 빠꿀때 동일해질 수 있냐가 문제
# 해당 코드는 새로운 문자를 넣는 경우를 마지막 길이 비교로 해결함
# 만약 길이 차이가 1이라면 1개의 문자를 넣어주면 해결되는 것임
# 아마 서로의 길이를 측정하여 각각의 경우에 따른 if문으로 걸러내는게 맞을 것임
# 단순히 길이비교로 따지면 case, wire의 길이는 각각 3, 3이 나오고 dog, god은 0, 0 이 나오므로
# 두 경우의 길이차는 각각 0임
# 각각의 경우를 구하면
# 둘의 길이가 0(동일), 둘의 길이가 1(빼고 더하기), 둘의 길이가 0, 1(하나 더 추가), 둘의 길이가 1, 0 (하나 빼기) 일때 일듯?

t = int(input())
target = list(input())  # pop 하기 위함
count = 0
for _ in range(t - 1):
    target_copy = target[:]  # pop 할 경우 원형 유지를 위함, 아니면 메모리에 직접 접근하는 것 같음
    word = list(input())
    for i in range(len(word)):
        cur = word.pop(0)
        if cur in target_copy:
            target_copy.remove(cur)
        else:
            word.append(cur)
    a = len(target_copy)
    b = len(word)
    # 각각의 경우를 구하면
    # 1. 동일한 경우
    # 2. 하나 빼고 하나 더하면 되는 경우
    # 3. 하나 빼면 되는 경우
    # 4. 하나 더하면 되는 경우
    if (a == 0 and b == 0) or (a == 1 and b == 1) or (a == 1 and b == 0) or (a == 0 and b == 1):
        count += 1
print(count)


# if
# target = dog => target_copy = dog
# word = doggy
# len(target_copy) == 0
# len(word) == 2 (앞부분을 빼가면서 했기 때문)