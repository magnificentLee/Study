movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "배트맨"]
del movie_rank[2 :]
print(movie_rank)
# del movie_rank[2 : 3] 이 안 먹히는 이유
# 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 합니다.
# 혹은
# del movie_rank[2]
# del movie_rank[2]
# 도 가능함