result = 0
print("Before", result)
numbers = [9, 41, 12, 3, 74, 15]
for i in range(len(numbers)):
    result += numbers[i]
    if i == len(numbers) - 1:
        print(result, numbers[i])
        break
    else:
        print(result, numbers[i])
print("After", result)
""" 기존
zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for thing in numbers :
    zork = zork + thing
    print(zork, thing)
print('After', zork
"""