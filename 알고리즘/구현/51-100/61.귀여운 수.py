# 등차 수열이므로 동일하게 증감하거나 유지된다는 점에 주목 +3 +3 +3 or +0 +0 +0 or -3 -3 -3
# 630의 경우 -3 -3이므로 절대값 3씩 변하므로 카운트하면 전체길이 -1 이 나옴
# 631의 경우 -3 -2 이므로 카운트하면 전체길이 -1 에 못 미침
# 입력값의 범위가 10^18 까지가기 때문에 리스트에 넣어서 비교하는 방식은 틀렸음
# idx 0, 1의 값을 비교하여 그 다음 값들이 그렇게 바뀌는지 비교하는 방법은 어떨까?
# 오답, 반례 : 0101 : 뀌요미로 나옴
"""
n = input()
tmp_list = []
l = len(n)
if l == 1:  # n = 한자리수일때 에러 방지를 위한 코드
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit(0)
for i in range(1, len(n)):
    tmp = abs(int(n[i]) - int(n[i - 1]))
    tmp_list.append(tmp)
if tmp_list.count(tmp_list[0]) == l - 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
"""
# 풀이2 : 정답 but 예쁘지 않음
"""
n = input()
l = len(n)
if l == 1:  # n = 한자리수일때 에러 방지를 위한 코드
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit(0)
tmp = int(n[0]) - int(n[1])  # 한 자리 수일 때 에러 방지를 위해 여기에 삽입
for i in range(1, l):
    if int(n[i - 1]) - int(n[i]) != tmp:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        break
else:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
"""
# 풀이3 : 예쁨
n = input()
l = len(n)
if l == 1:  # n = 한자리수일때 에러 방지를 위한 코드
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    tmp = int(n[0]) - int(n[1])  # 한 자리 수일 때 에러 방지를 위해 여기에 삽입
    for i in range(1, l):
        if int(n[i - 1]) - int(n[i]) != tmp:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
    else:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")