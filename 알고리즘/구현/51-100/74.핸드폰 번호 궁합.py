# 이전에도 풀어봤던 유형중 하나로 최종적으로 array[0], array[1] 에 결과가 저장된다는 점을 이용하는것
# 출력에서 조금 다른게 0을 그대로 붙인다는점을 놓쳐서 틀렸음
# 계속 이런 세세한 부분을 놓쳐서 틀리는데 주의해야할 필요가 있겠음
a = input()
b = input()
array = []
for i in range(8):
    array.append(int(a[i]))
    array.append(int(b[i]))
for _ in range(14):
    for i in range(15):
        array[i] = (array[i] + array[i + 1]) % 10
print(str(array[0]) + str(array[1]))