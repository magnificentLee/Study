import random

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", format(self.balance, ","))


p = Account("파이썬", 10000)
p.display_info()