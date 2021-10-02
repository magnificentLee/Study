c = {"a": 10,
     "b": 1,
     "c": 22}

tmp = list()
for k, v in c.items():
    tmp.append((k, v))
print(tmp)

tmp = sorted(tmp, key=lambda x: x[1])
print(tmp)
""" 기존방법
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp)
print(tmp)
"""