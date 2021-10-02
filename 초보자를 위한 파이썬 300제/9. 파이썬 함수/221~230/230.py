def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
# a, b 위치가 바뀌긴 했지만
# a, b 값을 지정해서 줬기 때문에 결과는 정상적으로 출력된다
# 왼쪽: 200
# 오른쪽: 100