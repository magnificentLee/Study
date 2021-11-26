# 수열의 길이가 전부 3이라는 점, 연속된 길이 3만큼씩 비교하면서 앞으로 진행하면 된다는점
for _ in range(int(input())):
    n = input()
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(40):
        result[0] += n[i:i + 3].count("TTT")
        result[1] += n[i:i + 3].count("TTH")
        result[2] += n[i:i + 3].count("THT")
        result[3] += n[i:i + 3].count("THH")
        result[4] += n[i:i + 3].count("HTT")
        result[5] += n[i:i + 3].count("HTH")
        result[6] += n[i:i + 3].count("HHT")
        result[7] += n[i:i + 3].count("HHH")
    print(*result)