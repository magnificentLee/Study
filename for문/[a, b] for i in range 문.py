score = [[int(input()), i+1] for i in range(8)]
print(score)
# 결과
# [[20, 1], [30, 2], [50, 3], [48, 4], [33, 5], [66, 6], [0, 7], [64, 8]]
# score = sorted(score) 할 경우
# [[0, 7], [20, 1], [30, 2], [33, 5], [48, 4], [50, 3], [64, 8], [66, 6]]
# 즉, i 까지 출력하는데 최적화
# lambda를 사용하는 경우
# score = sorted(score, key = lambda x: -x[0])
# [[66, 6], [64, 8], [50, 3], [48, 4], [33, 5], [30, 2], [20, 1], [0, 7]]
# score[0][0] = 66, score[0][1] = 6
