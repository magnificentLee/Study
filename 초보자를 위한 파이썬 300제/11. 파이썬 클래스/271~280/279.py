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
        self.deposit_count = 0

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", format(self.balance, ","))


account_list = []

a = Account("김철수", 500)
b = Account("김영희", 1000)
c = Account("정민", 1000000)

# account_list.extend([a, b, c]) 혹은
account_list.append(a)
account_list.append(b)
account_list.append(c)

for i in account_list:
    if i.balance >= 1000000:
        i.display_info()
