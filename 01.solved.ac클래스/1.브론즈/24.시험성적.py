n = int(input())
if n >= 90:
    print("A")
elif n >= 80:
    print("B")
elif n >= 70:
    print("C")
elif n >= 60:
    print("D")
else:
    print("F")
""" 궁금한점
>= 90 일 때는 68ms
> 89 일 때는 76ms
속도가 더 빨리 나올 줄 알았는데 더 느리게 나오는 이유?
"""