# 최솟값을 저장하는 변수에 아주 큰 값을 할당해야 할 때
# 일반적인 경우
"""
min_val = 99999
min_val > 10000000 # ?
"""
# 파이썬만의 방법
"""
min_val = float("inf")
min_val > 10000000000
"""
# inf에 음수를 붙이기도 가능
