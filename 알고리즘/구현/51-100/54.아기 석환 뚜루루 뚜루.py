song = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", "turu",
        "in", "bed", "tururu", "turu", "baby", "sukhwan"]  # 1사이클 = 14
n = int(input())
idx = (n % 14) - 1
count = n // 14
if "tu" not in song[idx]:
    print(song[idx])
else:  # "tu" in song[idx]
    target = song[idx] + "ru" * count
    target_count = target.count("ru")
    if target_count < 5:
        print(target)
    else:
        print("tu+ru*%i" % target_count)