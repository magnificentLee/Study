import pandas as pd

df = pd.DataFrame(
    {"a": [4, 5, 6, 4],
     "b": [7, 8, 9, 9],
     "c": [10, 11, 12, 10]},
    index=[1, 2, 3, 4])

# a 컬럼 값을 Groupby 하여 b 컬럼값 평균값 구하기
df = df.groupby(["a"])["b"].mean()  # 어째서 int가 아닌 float?
print(df)
# pivot_table로 평균값 구하기
print(pd.pivot_table(df, index="a"))
print(df)