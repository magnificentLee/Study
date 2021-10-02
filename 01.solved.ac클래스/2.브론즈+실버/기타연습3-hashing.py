from sys import stdin
input = stdin.readline

def hashing(n):
    result = 0
    for i in range(len(n)):
        dot = ord(n[i]) - 96
        result = (result + dot * (31 ** i)) % 1234567891
    return result

if __name__ == "__main__":
    t = int(input())
    n = input().strip()  # strip을 안 써줄 경우 공백까지 계산하기 때문에 전혀 다른 답이 나옴
    res = hashing(n)
    print(res)
# 그대로 제출할 경우 50점이 나옴(문자열이 길어질 경우 통과하지 못함)
# 기존 result 와 더해주는 부분을 고침
# 기존 : result += (dot * (31 ** i)) % 1234567891
# 수정 : result = (result + dot * (31 ** i)) % 1234567891
