import datetime

now = datetime.datetime.now()

for i in range(5, 0, -1):
    delta = datetime.timedelta(days=i)
    date = now - delta
    print(date)
# delta = 5,4,3,2days, 1day
# date = 현재날짜 - date(5~1일)
#2021-01-02 18:40:47.896221
#2021-01-03 18:40:47.896221
#2021-01-04 18:40:47.896221
#2021-01-05 18:40:47.896221
#2021-01-06 18:40:47.896221