num = 0
total = 0.0
while True:
    s_val = input("Enter a number: ")
    if s_val == "done":
        break
    # noinspection PyBroadException
    try:
        f_val = float(s_val)
    except:
        print("Invalid input")
        continue
    num += 1
    total += f_val
print(total, num, total/num)