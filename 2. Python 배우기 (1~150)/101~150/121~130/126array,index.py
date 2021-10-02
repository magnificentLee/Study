# a b c d e f g h i j k l m n o p q r s t u v w x y z
# 1 2 3 4 5 6 7 8 910 1 2 3 4 5 6 7 8 920 1 2 3 4 5 6 (-1씩 해주면 됨)
# 즉, 주어진 문자열을 알파벳 순서에 대응해서 숫자로 표현
# index 함수를 사용하면 될 것
"""
Input
baekjoon
Output
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 : x ~ z
"""
alpha_list = list("abcdefghijklmnopqrstuvwxyz")

lang = list(input())
array = [-1 for i in range(len(alpha_list))]

for i in range(len(lang)):
    if array[alpha_list.index(lang[i])] == -1:
        array[alpha_list.index(lang[i])] = i
for j in array:
    print(j, end=" ")
"""
alpha_list 의 요소들을 -1로 바꾼 array를 생성
alpha_list = "a","b","c"..."x","y","z"
lang = "b","a","e","k","j","o","o","n"
i = 0 -> lang[0] = "b", alpha_list.index("b") = 1, array[1] = 0 따라서 -1 0 -1 -1- 1...-1
i = 1 -> lang[1] = "a", alpha_list.index("a") = 0, array[0] = 1 따라서  1 0 -1 -1 -1...-1
i = 2 -> lang[2] = "e", alpha_list.index("e") = 4, array[4] = 2 따라서  1 0 -1 -1  2...-1
...
i = 7 -> lang[7] = "n", alpha_list.index("n") = 13, array[13] = 7 따라서 -1 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7...-1
"""