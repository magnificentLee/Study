string = input().upper()
# set 함수는 단일값들이 모여있는 자료형. 리스트와 비슷해보이지만 리스트처럼 단일요소의 값을 출력하는 건 불가능
# 따라서 list화 하지 않으면 제일 아래 출력단락에서 "not subscriptable" 에러가 발생함
word = list(set(string))
result = []
for i in word:
    result.append(string.count(i))
flag = result.count(max(result))
if flag > 1:
    print("?")
else:
    print(word[result.index(max(result))])
# 이전에 작성한 코드들보다 훨씬 간결하고 알아보기 쉽고 속도도 빠름
