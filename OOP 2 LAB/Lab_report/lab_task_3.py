class BankAccount:
    total_accounts = 0 

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0
        BankAccount.total_accounts += 1 

    def deposit(self, amount):
        if amount > 0: 
            self.balance += amount
            print(f"{self.owner_name} deposited: {amount}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds for {self.owner_name}. Withdrawal amount: {amount}, Current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"{self.owner_name} withdrew: {amount}. Current balance: {self.balance}")

    def show_balance(self):
        return self.balance

bank = BankAccount("Rafi")
bank1 = BankAccount("Havlu")

bank1.deposit(20000)
bank.deposit(10000)

bank1.withdraw(10000)
bank.withdraw(200)

print(f"Name: {bank.owner_name}, Balance: {bank.show_balance()}")
print(f"Name: {bank1.owner_name}, Balance: {bank1.show_balance()}")
print(f"Total Accounts: {BankAccount.total_accounts}")
