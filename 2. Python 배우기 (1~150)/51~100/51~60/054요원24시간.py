c = input().split(":")  # current_time
s = input().split(":")  # start_time
c_time = int(c[0]) * 3600 + int(c[1]) * 60 + int(c[2])
s_time = int(s[0]) * 3600 + int(s[1]) * 60 + int(s[2])
if c_time > s_time:
    e_time = (s_time + 24 * 3600) - c_time # estimate_time
else:
    e_time = s_time - c_time
h = e_time // 3600
m = (e_time % 3600) // 60
s = (e_time % 3600) % 60
h1 = str(h).zfill(2)
m1 = str(m).zfill(2)
s1 = str(s).zfill(2)
print("{}:{}:{}".format(h1, m1, s1))
# zfill 초보자 271번 참고