# 데이터를 찾기 위해 리스트 앞에서부터 하나씩 차례대로 확인하는 방법
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:  # 타겟 위치 확인
            return i + 1  # 인덱스는 0부터 시작하므로
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()  # 입력 = "숫자 문자열"
n = int(input_data[0])  # 숫자
target = input_data[1]  # 문자열
print("앞에 적은 원소 개수만큼 문자열을 입력하세요.")
array = input().split()
print(sequential_search(n, target, array))
#입력값
"""
5 Dongbin
Hanul Jonggu Dongbin Taeil Sangwook
"""