t = int(input())

for i in range(t):
    n = int(input())
    score = 0
    grade = 0

    for j in range(n):
        c, g = map(float, input().split())  # c : 학점, g : 성적
        score += c
        grade += c * g  # 성적 = sum(학점 * 성적)
    gpa = grade / score
    print(int(score), "%.1f" % gpa)
