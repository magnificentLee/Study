case = int(input())

for i in range(case):
    score_list = list(map(int, input().split()))
    score_avg = sum(score_list[1:]) / score_list[0] # 0: 학생숫자, 1부터 학생 점수
    std_avg_count = 0
    for j in score_list[1:]:
        if j > score_avg:
            std_avg_count += 1
    print("%.3f"% round(std_avg_count / score_list[0] * 100, 3) + "%")
    # round(a, b) : a를 소숫점 b+1 에서 반올림