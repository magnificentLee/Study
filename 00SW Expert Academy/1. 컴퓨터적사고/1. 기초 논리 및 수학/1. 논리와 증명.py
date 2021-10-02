# 토플 inclusive or : 둘 다 가능한 or
# 합격하려면 토플 500점 이상 혹은 토익 600점 이상

# 복권 exclusive or : 둘 중 하나만 가능한 or
Prize = True
while True:
    if Prize:
        print("상품을 선택하시오.:")
        print("번호를 입력하시오.: 1.자동차, 2.천만원")
        n = int(input())
        if n == 1:
            print("자동차를 얻었습니다.")
            break
        elif n == 2:
            print("천만원을 얻었습니다.")
            break
        else:
            print("오류가 발생했습니다.")
            continue
