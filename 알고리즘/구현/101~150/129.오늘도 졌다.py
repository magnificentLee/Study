# 울림 제미니스 array1
# 스타트링크 걸리버스 array2
# 각각의 리스트는 초, 말에 제미니/스타트 가 얻은 득점임
# 초에선 제미니의 점수를 더해서 스타트와 비교하고 말에선 스타트의 점수를 더해줌
# 다음 반복에서 2회차 초 제미니의 점수를 더한것과 1회말에서 스타트의 점수를 더한것을 비교해주는 식
# 울림 제미니스 역전패 : YES / 아니라면 : NO
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
tmp1, tmp2, flag = 0, 0, 0
for i in range(9):
    tmp1 += array1[i]
    if tmp1 > tmp2:
        flag = 1
    tmp2 += array2[i]
if tmp1 < tmp2 and flag == 1:
    print("Yes")
else:
    print("No")