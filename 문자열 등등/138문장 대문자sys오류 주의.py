# 문제를 제대로 파악하자
# 문장의 제일 처음 이후론 변하지 않는다 따라서 문장을 나누는게 포인트
t = int(input())

for i in range(t):
    lang = input()
    lang = lang[0].upper() + lang[1:]
    print(lang)

# sys.stdin.readline() 을 쓸 경우 정답이 나오긴 하지만 출력 형식 문제로 오답처리된다.