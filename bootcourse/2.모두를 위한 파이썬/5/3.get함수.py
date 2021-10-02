years = {"a": 2012,
         "b": 2018,
         "c": 2021}

c = years.get("c", "Nothing")
d = years.get("d", "Nothing")
print(c, d, sep="\n")

# key 값을 호출, 만약 있으면 value를 가져오고 없으면 Nothing을 출력