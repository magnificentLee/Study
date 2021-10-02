# Categorical 한 값의 빈도수를 구하는 방법
import pandas as pd

df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]},
    index=[1, 2, 3])

print(df["a"].value_counts())
print(df[["a"]].value_counts())