class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
        
account = BankAccount("Joe", 10000) 

account.deposit(5000)
account.withdraw(1200)

print (account.owner)
print (account.balance)   