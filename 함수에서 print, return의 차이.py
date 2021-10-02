"""def print_sum(a, b):
    print(a + b)
    # 완료후 None으로 대체됨
    # 즉, 지금 당장의 함수에서만 결과가 나오고 이후엔 활용 불가능
print(print_sum(2, 4))"""
def return_sum(a, b):
    return a + b
# 완료후 함수 return_sun()은 a + b 즉 6으로 대체되기 때문에
# 다음 계산에서 같은 값으로 사용할 수 있다
print(return_sum(2, 4))

# 결론
# 당장의 결과만 출력하고 싶다 = print
# 이후 계산에서 사용하고 싶다 = return