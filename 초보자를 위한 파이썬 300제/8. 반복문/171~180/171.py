"""price_lost = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_lost[i])"""
# 더 좋은 코드 : price_list 가 변해도 코드의 수정 필요X
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])