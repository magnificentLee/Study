# 파일의 주소를 복사
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\extra\Desktop\Programming\의료기관_201909\상가업소정보_의료기관_201909.csv", low_memory=False, encoding="cp949")
print(np.shape(df))

