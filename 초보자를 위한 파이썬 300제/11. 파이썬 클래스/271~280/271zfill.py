import random

class Account:
    def __init__(self, name, balance): #balance:잔고
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3) # "1" -> "001"
        num2 = str(num2).zfill(2) # "1" -> "01"
        num3 = str(num3).zfill(6) # "1" -> "000001"
        self.account_number = num1 + "-" + num2 + "-" + num3

kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)