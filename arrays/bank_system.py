"""
You have been tasked with writing a program for a popular bank that will automate 
all its incoming transactions (transfer, deposit, and withdraw).
The bank has n accounts numbered from 1 to n. 
The initial balance of each account is stored in a 0-indexed integer array balance,
with the (i + 1)th account having an initial balance of balance[i].
"""
class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) or account2 > len(self.balance) or self.balance[account1-1] < money:
            return False
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            self.deposit(account1, money)
            return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance) or self.balance[account-1] < money:
            return False
        self.balance[account-1] -= money
        return True        