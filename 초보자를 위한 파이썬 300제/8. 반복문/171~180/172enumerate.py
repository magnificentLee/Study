"""price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(i, price_list[i])"""
# 더 좋은 코드
price_list = [32100, 32150, 32000, 32500]
for i, j in enumerate(price_list):
    print(i, j)