# 수가 입력되지 않아서 에러가 발생하면 반복문을 끝낼 수 있도록 try except
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# 에러가 발생하는건 제대로 작성한 코드가 아님
# 일반적인 코드처럼 종료되는게 정상임