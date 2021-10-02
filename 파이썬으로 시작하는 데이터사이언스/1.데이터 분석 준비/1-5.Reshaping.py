# 특정 컬럼을 기준으로 정렬하기
import pandas as pd

df = pd.DataFrame(
    {"a": [4, 5, 6, 4],
     "b": [7, 8, 9, 9],
     "c": [10, 11, 12, 10]},
    index=[1, 2, 3, 4])

# a 컬럼을 기준으로 정렬하기
"""
df = df["a"].sort_values()
print(df)
"""
# DataFrame 전체에서 a 값을 기준으로 정렬하기
"""
df = df.sort_values("a")
print(df)
"""
# 역순으로 정렬하기
"""
df = df.sort_values("a", ascending=False)
print(df)
"""
# c컬럼 drop 하기
df = df.drop(["c"], axis=1)
print(df)