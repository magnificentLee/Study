# 65~90 : A~Z
# 계수정렬을 이용
# 각 for문을 돌 때 대문자화하게 만들었음 -> 불필요한 반복문 순환 방지
import sys

for i in range(int(input())):
    n = sys.stdin.readline()
    array = [0] * 26
    for j in n:
        idx = ord(str(j).upper()) - 65
        if 0 <= idx <= 25:
            array[idx] += 1
    check = min(array)
    if check == 0:
        print("Case {}: Not a pangram".format(i + 1))
    elif check == 1:
        print("Case {}: Pangram!".format(i + 1))
    elif check == 2:
        print("Case {}: Double pangram!!".format(i + 1))
    else:
        print("Case {}: Triple pangram!!!".format(i + 1))
