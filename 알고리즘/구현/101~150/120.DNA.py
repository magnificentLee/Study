# 각각의 DNA들을 비교하여 오차(같지 않은)가 가장적은 DNA를 선택하는 문제인줄 알았지만
# 정답은 주어진 DNA의 각 열을 비교하여 가장 많이 나온 값을 이용해 DNA를 만드는 것으로
# 새로 만든 DNA와 기존 DNA를 비교했을때 차이가 생긴만큼 더해주는것
# 각 열에서 최다 카운트
# 각 열에서 최다 카운트후 (열의 길이 - 최다 카운트) 를 합쳐주면 Hamming Distance의 합이 나올것임
n, m = map(int, input().split())
array = [input() for _ in range(n)]
dna = ["A", "C", "G", "T"]
result = ""
count = 0
for i in range(m):
    dna_count = [0, 0, 0, 0]
    for j in range(n):
        if array[j][i] == "A":
            dna_count[0] += 1
        elif array[j][i] == "C":
            dna_count[1] += 1
        elif array[j][i] == "G":
            dna_count[2] += 1
        else:
            dna_count[3] += 1
    result += dna[dna_count.index(max(dna_count))]
    count += n - max(dna_count)
print(result, count, sep="\n")


# 중복 될 경우를 준비
# 아래 코드를 테스트 해본 결과 가장 앞이 우선을 나옴
"""
dna = ["A", "C", "G", "T"]
dna_count = [1, 1, 3, 3]
print(dna[dna_count.index(max(dna_count))])
"""
# 처음 구현, 문제를 완전히 잘못이해했음
"""
n, m = map(int, input().split())
array = [input() for _ in range(n)]
result = []
for i in range(n):
    tmp = 0
    for j in range(1, n):
        for k in range(m):
            if array[0][k] != array[j][k]:
                tmp += 1
    array.append(array[0])
    result.append((array[0], tmp))
    del array[0]
print(array)
print(result)

TAAGCTAC

AAAGATCC 3
TGAGATAC 2
TAAGATGT 3
TATGATAC 3
"""