import random


class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3
        self.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_log.append(amount)

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdraw_log.append(amount)

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", format(self.balance, ","))

    def deposit_history(self):
        print("입금기록")
        for i in self.deposit_log:
            print(i)
        print("-" * 5)

    def withdraw_history(self):
        print("출금기록")
        for i in self.withdraw_log:
            print(i)
        print("-" * 5)


k = Account("Kim", 1000)
k.deposit(300)
k.deposit(600)
k.deposit(1000)
k.deposit_history()

k.withdraw(200)
k.withdraw(300)
k.withdraw(500)
k.withdraw_history()