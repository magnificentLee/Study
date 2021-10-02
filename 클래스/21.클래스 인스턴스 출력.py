# 일반적인 방식 or 다른 언어
"""
class Coord(object):
    def __init__(self, x, y):
        self.x, self.y, = x, y

point = Coord(1, 2)
print("({}, {})".format(point.x, point.y))
"""
# 파이썬만의 기능
class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

point = Coord(1, 2)
print(point)