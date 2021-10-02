numbers = [9, 41, 12, 3, 74, 15]
for i in range(len(numbers)):
    if i == 0:
        print("Before", i)
    elif i == len(numbers) - 1:
        print("After", i)
    else:
        print(i, numbers[i])
""" 기존
zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for thing in numbers :
    zork = zork + 1
    print(zork, thing)
print('After', zork)
"""