# 문자 A, B가 주어질때 A의 알바펫 순서를 바꾸면 B를 만들 수 있을때 A와 B를 애너그램이라 함

# 반복문으로 비교할 필요도 없음, 길이를 비교할 필요도 없음
# 두 값을 정렬하여 비교하면 따로 비교할 필요도 없음
for _ in range(int(input())):
    a, b = input().split()
    if sorted(a) == sorted(b):
        print("{} & {} are anagrams.".format(a, b))
    else:
        print("{} & {} are NOT anagrams.".format(a, b))

# 복수의 테스트를 진행할 경우 공백이 입력되면 에러가 발생, 이 부분을 수정했지만 여전히 오답출력
# 다른 사람의 코드를 참고한 결과 공백 입력은 문제가 아님. 아마 다른 반례가 존재하는 것 같음
"""
t = int(input())
for _ in range(t):
    try:
        a, b = input().split()
        len_a, len_b = len(a), len(b)
    except:
        continue
    flag = 0
    if len_a != len_b:  # 길이가 달라 애너그램이 될 수 없는 경우
        print("{} & {} are NOT anagrams.".format(a, b))
        continue
    for i in b:
        if i in a:
            len_a -= 1
    if len_a == 0:  # 길이는 같지만 애너그램이 아닌 경우
        print("{} & {} are anagrams.".format(a, b))
    else:
        print("{} & {} are NOT anagrams.".format(a, b))
"""
# 틀렸던 풀이
"""
# 만약 길이를 초과한다 -> 애너그램X
# 길이를 초과하지 않을 때 반복문을 돌려 flag 를 1 씩 증가, 길이와 동일해질 경우 애너그램, 아닐 경우 애너그램X
# 생각해보니 굳이 flag를 또 안 써도 될 것 같음
# 이미 이전에 길이를 비교했기 때문에 길이 비교값에 -1씩 해줘서 0이 될 경우 애너그램이라는 것을 출력하면 될 것 같음
t = int(input())
for _ in range(t):
    a, b = input().split()
    len_a, len_b = len(a), len(b)
    flag = 0
    if len_a != len_b:  # 길이가 달라 애너그램이 될 수 없는 경우
        print("{} & {} are NOT anagrams.".format(a, b))
        continue
    for i in b:
        if i in a:
            len_a -= 1
    if len_a == 0:  # 길이는 같지만 애너그램이 아닌 경우
        print("{} & {} are anagrams.".format(a, b))
    else:
        print("{} & {} are NOT anagrams.".format(a, b))
# 코드에 not 을 출력하는 부분이 중복되기 때문에 좀 지저분해보임
# 한 문자열에 최대 100자까지 나올 수 있기 때문에 하나로 통합해도 시간은 크게 차이나지 않을 것 같음
"""