t = int(input())

for i in range(t):
    a = int(input())
    bin_a = list(bin(a))[:1:-1]
    result = ""
    for j, bn in enumerate(bin_a):
        if bn == "1":
            result += str(j) + " "
    print(result.rstrip())  # 마지막의 오른쪽 공백을 없애기 위함

# print(j, bn)
"""
Input 1 / 13
Output 
enumerate : j, bn
0 1
1 0
2 1
3 1
"""