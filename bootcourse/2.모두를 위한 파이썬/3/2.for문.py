largest_so_far = -1
print("Before", largest_so_far)
numbers = [9, 41, 12, 3, 74, 15]

for the_num in numbers:
    if the_num > largest_so_far:
        largest_so_far = the_num
        # 기존 print('largest_so_far: ', largest_so_far, 'current number: ',the_num)
    print("largest_so_far: {} current number: {}".format(largest_so_far, the_num))
print("After", largest_so_far)