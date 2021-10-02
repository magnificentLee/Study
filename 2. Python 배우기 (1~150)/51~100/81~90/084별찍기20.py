# i가 짝수일때는 "* ", 홀수 일때는 " *"
n = int(input())

for i in range(n):
    if i % 2 == 0:
        print("* " * n)
    else:  # i % 2 == 1 즉, 홀수인 경우
        print(" *" * n)
