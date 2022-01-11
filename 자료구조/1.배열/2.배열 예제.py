# 특정 데이터 세트에서 특정한 알파벳이 몇 번이나 사용되었는지 찾아보는 함수
def find_alphabet(array, alphabet):
    count = 0
    for data in array:
        for i in range(len(data)):
            if data[i] == alphabet:
                count += 1
    print(count)


dataset = ["abcd", "efgh", "abcdabcd", "Abcdabcdabcd"]  # 소문자만 총 5개
find_alphabet(dataset, "a")  # 5 출력

