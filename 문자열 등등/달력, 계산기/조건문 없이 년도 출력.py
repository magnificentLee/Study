# 1, 4, 14 ... 99 까지 년도를 20XX로 출력하는 법

year = int(input())
print("연도는 20%.2d" % year)

# 만약 조건문을 써야되면 아래처럼 길어질 것이다
if len(str(year)) == 1:
    year = "0" + str(year)
print("연도는 20%s" % year)
