# 두 숫자 R1과 R2가 있을 때, 두 수의 평균 S는 (R1+R2)/2와 같다.
# 첫째 줄에 두 정수 R1과 S가 주어진다
# 첫째 줄에 R2를 출력한다.
r1, s = map(int, input().split())
print(2 * s - r1)
