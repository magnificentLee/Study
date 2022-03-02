# 특정 값을 제거해야 하므로 pop이 아닌 remove를 쓰는게 나을것
# 같은 스티거가 없으면 붙이고 있으면 뜯는다, 이런 과정을 반복할 때 스티커가 최대로 붙어 있는 갯수를 구하라는 것
# 다른 방법으로 2로 나누어 떨어지면 이미 붙어있다는 점을 이용할 수 있지 않을까
# 0인 경우와 2인경우 모두 똑같은 결과가 나오므로 2로 나누는 것보다 True False 리스트를 만드는게 나을 것
# 매순간순간의 최댓값을 구해야하기 때문에 정렬해서 하는 방식은 통하지 않을 것임
n = int(input())
array = list(map(int, input().split()))
menu = [False] * 100001
max_count = 0
tmp_count = 0
for i in array:
    if not menu[i]:
        tmp_count += 1
        menu[i] = True
    else:
        tmp_count -= 1
        menu[i] = False
    if max_count < tmp_count:
        max_count = tmp_count
print(max_count)

# 조금 다른 방식
# count 리스트를 만들어 그때그때 길이값을 넣어 마지막으로 리스트에서 최대 길이를 뽑는 것
# 시간복잡도가 더 높을 것 같아서 if문으로 최댓값만 갱신하게끔 바꿨음
# 아래 코드는 시간초과가 발생할것임
"""
n = int(input())
array = list(map(int, input().split()))
menu = []
count = []
for i in range(2 * n):
    tmp = array[i]
    if tmp in menu:
        menu.remove(tmp)
    else:
        menu.append(tmp)
    count.append(len(menu))
print(max(count))
"""