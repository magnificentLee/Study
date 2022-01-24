# 팰린드롬인지 확인
# 만약 리스트의 길이가 짝수라면 각각의 요소들이 짝수 개수를 이루는가?
# 만약 리스트의 길이가 홀수라면 하나를 제외한 나머지는 짝수 개수를 이루는가?
# 짝수 : ABAB = ABBA, ABCD != 팰린, ABCDABCD = ABCDDCBA ...
# 홀수 : ABCAB = ABCBA, ABCAD != 팰린. ABCABCD = ABCDCBA ...
# 짝수, 홀수를 통합 : 만약 홀수인 요소가 1개보다 많다면 = 불가능 출력

# 판별하는 방법은 위와 같은것 같고 어떻게 순서 + 역순으로 배치할 수 있을까
# 글자는 최대 50글자로 구성됨, 대문자로만 구성
# 정답일 때는 정답인 팰린드롬을 출력, 불가능하면 I'm Sorry Hansoo 를 출력, 정답이 여러개면 사전순으로 앞서는 것을 출력
name = input()
alp = [0] * 26
flag = 0
left = ""
center = ""
for i in set(name):
    idx = ord(i) - 65
    alp[idx] += name.count(i)
for i in range(26):
    if alp[i] % 2 != 0:
        flag += 1
        center += chr(i + 65)
    left += chr(i + 65) * (alp[i] // 2)
    if flag > 1:
        break
right = left[::-1]
if flag > 1:
    print("I'm Sorry Hansoo")
else:
    print(left + center + right)