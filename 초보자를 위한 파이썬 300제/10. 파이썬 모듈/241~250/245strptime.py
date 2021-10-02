# datetime.datetime.strptime('날짜문자열', '포맷')
#strptime 메서드를 사용하면 문자열 형태의 날짜를
# datetime.datetime 객체로 만들 수 있습니다
import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))
