N = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
result = []
for i in range(N):
    result.append(arr1[i] | arr2[i])
for i in range(N):
    var = bin(result[i]).split("b")
    var = var[1].zfill(N).replace("1", "#").replace("0", " ")
    result[i] =var

print(result)

