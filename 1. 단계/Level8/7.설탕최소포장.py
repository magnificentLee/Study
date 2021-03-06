""" 코딩 전 생각
1. 3과 5로 각각 나누어 몫을 비교, 제일 낮은 숫자를 이용하는 방법
=> if문이 계속 늘어날 것이라 예상하여 포기
2. 5로 나누고 5을 빼는 방법
=> 3의 배수중 일부는 먹히지 않음
3. 5로 나누는 건 if문으로 처리 => if n % 5 == 0
결론. 애초에 3을 빼서 5의 배수인지 확인하면 됨!
"""
n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:  # n이 5의 배수일 때
        count += n // 5  # 몫 = 5로 나눈 개수
        print(count)
        break
    n -= 3  # 5의 배수가 아니면 계속 3을 뺄 것임 -> 어느 순간 0보다 낮아지므로 while문 탈출
    count += 1
else:  # 0보다 낮아져 while문을 탈출한 경우 (3, 5 로 구할 수 없는 경우)
    print(-1)
