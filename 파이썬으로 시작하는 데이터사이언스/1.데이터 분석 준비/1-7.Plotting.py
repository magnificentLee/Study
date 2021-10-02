# 에러 발생 대체 왜?
# matplotlib 라이브러리를 설치하지 않았었기 때문 -> 해결
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {"a": [4, 5, 6, 4],
     "b": [7, 8, 9, 9],
     "c": [10, 11, 12, 10]},
    index=[1, 2, 3, 4])

plt.plot(df)
df.plot.bar()
df.plot.density()
plt.show()