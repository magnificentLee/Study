# 라이브러리를 사용하지 않는 경우
"""
data = ["A", "B", "C"]
data_list = []
for i in data:
    for j in data:
        for k in data:
            if i != j and j != k and i != k:
              data_list.append([i, j, k])
for i in data_list:
    print(i, end=",")
"""
# 라이브러리를 사용하는 경우
from itertools import permutations
from itertools import combinations

data = ["A", "B", "C"]

result = list(permutations(data, 3))

print(result)
# 결과 = [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
# 즉, 원소를 중복하진 않음 (A, A, A) 같이
# 조합의 경우
"""
from itertools import combinations
    
data = ["A", "B", "C"]

result = list(combinations(data, 3))

print(result)
"""
# 결과 : [('A', 'B', 'C')]
# 즉, a, b, c의 순서에 상관없이 중복된 결과는 제외하고 출력한다는 말

# product
"""
from itertools import product

data = ["A", "B", "C"]
result = list(product(data, repeat=2))
print(result)
"""
# 결과 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
# 모든 경우의 수를 계산하는데 원소를 중복하여 뽑음

# combinations_with_replacement
# 순서에 상관없이 원소를 중복하여 모든 경우를 뽑음
"""
from itertools import combinations_with_replacement

data = ["A", "B", "C"]
result = list(combinations_with_replacement(data, 2))
print(result)
"""
# 결과 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
