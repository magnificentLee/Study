ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total = 0
for i in ohlc[1:]:
    total += i[3] - i[0]
print(total)