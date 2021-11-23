# if문으로 각각의 경우를 설정해주는 방법이 있지만 코드의 길이가 쓸데없이 길어짐
# 딕셔너리로 1대1 대응을 시켜주면 짧게 줄일 수 있다
# key: value 에서 각각의 key값을 만들어주긴 해야함 ex) {"a": "A", "A": "a"}
# 우쨋든 딕셔너리를 사용하면 if문 보다는 훨씬 간결함

# initial data
milk_code = {".": ".", "O": "O", "-": "|", "|": "-", "/": "\\", "\\": "/", "^": "<", "<": "v",
             "v": ">", ">": "^"}
n, m = map(int, input().split())
milk = [list(input()) for _ in range(n)]  # milk = 2중 리스트
result = []
for i in zip(*milk):  # i = 리스트
    tmp = [milk_code[j] for j in i]
    result.append(tmp)
# 왼쪽으로 엎어야 하기 때문에 기존 1열의 문자들은 마지막행에서,
# 가장 오른쪽 열은 1행에서 출력되야함 따라서 reverse로 뒤집어서 출력
# 단, re_list = reversed(list)를 쓰지 말것 -> 메모리 주소가 출력됨
for i in reversed(result):
    print(*i, sep="")

"""
zip:X   zip:O
..>...  ../^\..
/|||\.  ./---\.
v...-\  .|...|.
v.O.-^  <|.O.|>
v...-/  .|...|.
\|||/.  .\vvv/.
..<...
"""