"""
num = int(input().strip())
num_list = list(range(65, 91))
alpha = [chr(i) for i in num_list]
if num == 0:
    print(*alpha, sep="")
else:
    alpha_up = [i.lower() for i in alpha]
    print(*alpha_up, sep="")
"""
num = int(input().strip())
num_list = list(range(65, 91))
if num == 1:
    result = [chr(i).upper() for i in num_list]
elif num == 0:
    result = [chr(i).lower() for i in num_list]
print(*result, sep="")