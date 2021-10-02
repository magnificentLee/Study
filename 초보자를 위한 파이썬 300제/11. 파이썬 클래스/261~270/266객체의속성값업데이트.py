class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


삼성 = Stock("삼성전자", "005930", 1, 1, 1.0)
print(삼성.name, 삼성.code,
      삼성.per, 삼성.pbr, 삼성.배당수익률,
      삼성.get_name(), 삼성.get_code(), sep="\n")
