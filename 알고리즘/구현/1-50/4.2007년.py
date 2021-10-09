# 지나간 달 * 지나간 달의 날짜 + y일이고 입력값의 범위는 1~12 즉, 12월까지이므로
# 마지막 달(12월)은 인덱스에 넣을 필요가 없음 (12월31일은 1~11월까지의 일수와 31일을 더하면 되기 때문)
d = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]  # day
m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]  # month
x, y = map(int, input().split())
result = sum(m[:x]) + y
day = result % 7
print(d[day])