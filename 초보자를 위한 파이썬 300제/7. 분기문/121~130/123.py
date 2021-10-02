num, currency = input("입력: ").split()
환율 = {"달러": 1167,
      "엔": 1.096,
      "유로": 1268,
      "위안": 171}
print(float(num) * 환율[currency])