# 자기 자신을 다시 호출하는 함수
# DFS/BFS 를 구현하기 위해선 필수임
def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()

recursive_function()

# 실행 할 경우
# "재귀 함수를 호출합니다." 문자열이 계속 나열되다 에러 발생
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀의 최대 깊이를 초과했다는 내용으로 파이썬 인터프리터는 호출 횟수 제한이 있기 때문임
# 애초에 무한한 재귀 호출을 요구하는 문제 또한 없음

# 재귀 함수는 프랙털 구조와 유사함 (삼각형 안에 삼각형이 계속 존재하는 삼각형)
# 실제로 프랙털 이미지를 출력하는 프로그램을 작성 할 때 재귀 함수를 이용함
