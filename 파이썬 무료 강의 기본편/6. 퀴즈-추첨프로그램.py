import random

users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)
random.shuffle(users) # users 를 섞음
winners = random.sample(users, 4) # users중 4명을 뽑아서 리스트에 저장
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0])) # 1명 치킨
print("커피 당첨자 : {}".format(winners[1:])) # 3명 커피
print(" -- 축하합니다 --")
