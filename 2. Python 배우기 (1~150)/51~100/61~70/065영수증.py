# 첫째 줄에 10권의 총 가격
# 둘째 줄부터 9개 줄에는 가격을 읽을 수 있는 책 9권의 가격
# 출력: 가격을 읽을 수 없는 책의 가격
total = int(input())
for i in range(9):
    a = int(input())
    total -= a
print(total)