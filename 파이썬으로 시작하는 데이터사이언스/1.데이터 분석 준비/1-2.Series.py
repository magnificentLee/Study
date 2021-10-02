import pandas as pd

df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=[1, 2, 3])

print(df["a"])  # 4, 5, 6 = Series 데이터
print(df[["a"]])  # DataFrame 형태로 출력
