# Eof 에러에 관해서 어떻게 처리하냐의 문제
while True:
    try:
        print(input())
    except EOFError:
        break
