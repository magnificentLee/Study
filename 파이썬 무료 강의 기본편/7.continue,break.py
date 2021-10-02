absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. %s는 교무실로 따라와" % no_book)
        break
    print("{}, 책을 읽어봐".format(student))
