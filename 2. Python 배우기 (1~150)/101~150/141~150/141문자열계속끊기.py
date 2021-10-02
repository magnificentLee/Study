lang = input()
while len(lang) > 10:
    print(lang[:10], end="\n")
    lang = lang[10:]
if len(lang) <= 10:
    print(lang)