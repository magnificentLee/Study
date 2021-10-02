# 한글 폰트 설정
# 알맞은 OS에 따라 plt.rc 소스를 실행, 해당하지 않는 OS의 소스는 주석처리
# 주석처리 단축키 : Ctrl(cmd) + /
import matplotlib.pyplot as plt

# minus 폰트 깨짐 방지
# 한글 폰트를 사용하면 minus font가 깨지는 경우가 있어 unicode_minus를 False로 설정
plt.rc("axes", unicode_minus=False)

# retina 설정 : 글씨의 선명도 증가 (해당 라이브러리 설치X 따라서 주석처리함)
# from IPython.display import set_matplotlib_formats
# set_matplotlib_formats("retina")
