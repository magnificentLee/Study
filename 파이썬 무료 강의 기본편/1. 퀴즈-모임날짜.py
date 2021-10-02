# 매월의 1~3일을 제외하고 최대 28일까지 랜덤으로 모임 날짜 출력
import random

date = random.randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")