# 문제 설명
# 123이라는 숫자가 주어질 때 이를 분해해보면 1, 2, 3 의 숫자가 된다.
# 이 숫자들은 등차수열을 이루므로 123은 한수이다.
# 1부터 9까지도 한수에 포함된다.
n = int(input())
han_su = 0
for i in range(1, n + 1):
    if len(str(i)) < 3:
        han_su += 1
    else:
        i_list = list(map(int, str(i)))
        if i_list[0] - i_list[1] == i_list[1] - i_list[2]:
            han_su += 1
print(han_su)
