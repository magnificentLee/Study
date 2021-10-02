# list(a) 를 할 경우 단일객체로 리스트화 불가 따라서 에러 발생
"""
answer = []
while True:
    a = int(input())
    a_list = []
    if a == -1:
        break
    for i in range(1, a):
        if a % i == 0:
            a_list.append(i)
    a_list = sorted(a_list)
    if a == sum(a_list):
        answer.append("{} = {}".format(a, "+".join(map(str, a_list))))
    else:
        answer.append("{} is not perfect.".format(a))


for i in answer:
    print(i)
"""
answer = []
while True:
    a = int(input())
    a_list = []
    if a == -1:
        break
    for i in range(1, a):
        if a % i == 0:
            a_list.append(i)
    a_list = sorted(a_list)
    if a == sum(a_list):
        answer.append("{} = {}".format(a, " + ".join(map(str, a_list))))
    else:
        answer.append("{} is NOT perfect.".format(a))


for i in answer:
    print(i)
