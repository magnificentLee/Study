# 백준 10867 중복 빼고 정렬하기
# k의 값이 크기 때문에 계수정렬 대신 집합과 sort 함수를 이용
# 단, 파이썬의 집합은 정렬된 상태가 아니므로 집합으로 만든 후 정렬시키는 과정도 필요할 것
n = int(input())
array = set(map(int, input().split()))
print(*sorted(array))