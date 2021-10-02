def pickup_even(string):
    my_list = []  # 결과값용 리스트
    for i in string:
        if int(i) % 2 == 0:  # 짝수 판정
            my_list.append(i)  # 참값인 경우 결과값 리스트에 저장
    return my_list  # 함수를 결과값용 리스트에 반환


print(pickup_even([3, 4, 5, 6, 7, 8]))
