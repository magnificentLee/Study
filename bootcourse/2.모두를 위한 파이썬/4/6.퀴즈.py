words = "Connect Foundation"

if "F" in words:
    words.lower()
    words[7] = "&"
else:
    print(words)
print("words")

"""
connect&foundation 이라는 결과를 예측했다면 틀렸음
리스트가 아니라 문자열이라 중간에 추가하는 방식은 에러가 발생함

"""