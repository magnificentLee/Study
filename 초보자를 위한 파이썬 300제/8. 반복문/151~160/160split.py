리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    j = i.split(".")[1]
    if j in ["h", "c"]:
        print(i)