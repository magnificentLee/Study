#입력 문자열을 한 줄에 다섯글자씩 출력하는
#print_5xn(string) 함수를 작성하라.


def print_5xn(string):
    num = int(len(string) / 5) #float 이기 때문에 int로
    for i in range(num):
        print(string[i * 5: i * 5 + 5])

print_5xn("아이엠어보이유알어걸")
