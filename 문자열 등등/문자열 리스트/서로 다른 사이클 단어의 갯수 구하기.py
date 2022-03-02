# 백준 1544 사이클 단어
# 사이클 단어 : 단어를 시계 방향으로 하나씩 옮겨가며 읽는 방식
# picture의 사이클 단어: icturep, cturepi, turepic, urepict, repictu, epictur
# 동일한 단어로 변환시키는 방식
# 참고로 빠른 입력을 사용해도 속도 차이가 없으며 오히려 메모리를 조금 더 사용하게 됨
from collections import deque

n = int(input())
array = [input() for _ in range(n)]
for i in range(n):
    word_list = deque(array[i])  # 검사용 변환된 단어들 저장용
    l = len(word_list)
    for j in range(l):
        word_list.append(word_list.popleft())
        word = "".join(word_list)
        if word == array[i]:
            break
        if word in array:
            idx = array.index(word)
            array.pop(idx)
            array.insert(idx, array[i])
print(len(set(array)))