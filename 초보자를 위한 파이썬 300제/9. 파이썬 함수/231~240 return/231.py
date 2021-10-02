def n_plus_1(n):
    result = n + 1

n_plus_1(3)
print(result)
# 결과는 에러 발생
# 함수 내부에서 사용한 변수는 함수 밖에서는 접근이 불가능함
# 함수 내부에서 계산한 값을 전달하기 위해선 return을 사용해야 한다.