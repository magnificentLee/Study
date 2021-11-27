# 케이스2, 케이스4 : 단순히 길이 비교X 라는뜻
# if len(a) == len(b) and set(a) == set(b) 로 비교하면 안 될 것임
# abbccd, aabccd 은 위에 해당되지만 다르기 때문임
# sorted로 비교하면 되지 않을까?
idx = 1
while True:
    a = input()
    b = input()
    flag = ""
    if a == "END" and b == "END":
        break
    if len(a) != len(b):
        flag = "different"
    else:
        if sorted(a) == sorted(b):
            flag = "same"
        else:
            flag = "different"
    print("Case {}: {}".format(idx, flag))
    idx += 1