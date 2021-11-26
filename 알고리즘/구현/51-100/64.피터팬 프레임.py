# 반례를 생각하며 각각의 경우를 생각하며 구현하기 힘들었던 문제

# 알파벳이 3의 배수일때가 아님
# 문자열에서 위치가 3의 배수일 때임
n = input()
l = len(n)
array = [".", ".", "#", ".", "."]
for i in range(l):
    if (i + 1) % 3 == 0:
        for j in range(5):
            if j == 0 or j == 4:
                array[j] += "..*.."
            elif j == 1 or j == 3:
                array[j] += ".*.*."
            elif j == 2:
                array[j] += "*." + n[i] + ".*"
    else:
        for j in range(5):
            if j == 0 or j == 4:
                array[j] += ".#."
            elif j == 1 or j == 3:
                array[j] += "#.#"
            elif j == 2:
                array[j] += "." + n[i] + "."
    if (i + 1) % 3 == 1:  # 프레임이 덜 완성된 1, 2 단계 사이
        for j in range(5):
            if j == 2:
                array[j] += "#"
            else:
                array[j] += "."
    if i == l - 1 and (i + 1) % 3 == 2:
        for j in range(5):
            if j == 2:
                array[j] += "#"
            else:
                array[j] += "."

for i in array:
    print(*i, sep="")