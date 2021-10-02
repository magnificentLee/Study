import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc["max_price"]) - float(btc["min_price"])
total = float(btc["opening_price"]) + 변동폭
if total > float(btc["max_price"]):
    print("상승장")
else:
    print("하락장")
# requests 오류로 실행불가