# `,q,a,z 는 입력에서 제외, 오른쪽으로 한 칸씩 이동한 상태로 쓴다는 것 = 왼쪽으로 대응시킬 것
# 입력은 여러줄이기 때문에 while문으로 처리하되 공백 입력시 종료되게, 다만 공백 입력시 대응해야될것
# 런타임 에러 발생 => if not n: break 문이 문제인것 같음, try except 문으로 바꿔보자
import sys
top = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="]
middle1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"]
middle2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"]
down = ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]

while True:
    n = sys.stdin.readline().rstrip()
    result = ""
    if n == "":
        break
    for i in n:
        if i in top:
            result += top[top.index(i) - 1]
        elif i in middle1:
            result += middle1[middle1.index(i) - 1]
        elif i in middle2:
            result += middle2[middle2.index(i) - 1]
        elif i in down:
            result += down[down.index(i) - 1]
        else:  # 공백인 경우
            result += " "  # 해당 부분이 런타임에러 발생시켰던것 같음, 원래는 result += i 였음
    print(result)