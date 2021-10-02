# 일부 값만 불러오기
import pandas as pd

df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=[1, 2, 3])

# 두 개 이상의 값을 불러올 때 Series 형태로 불러올 경우 에러가 발생하므로
# 아래와 같이 DataFrame 형태로 불러와야함
print(df[["a", "b"]])