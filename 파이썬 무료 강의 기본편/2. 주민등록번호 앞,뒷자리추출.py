jumin = "990120-1234567"
jumin = jumin[:jumin.index("-")] # 처음부터 주민인덱스의 - 전 까지
print(jumin)
""" 뒷자리만 가져오기
jumin = "990120-1234567"
jumin = jumin[jumin.index("-"):] # 주민인덱스의 -부터 끝까지
jumin = jumin.replace("-", "") # 처음 - 를 공백으로 대체
print(jumin)
"""