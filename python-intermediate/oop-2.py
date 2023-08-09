class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(
            f"Bank account with account number {self.account_number} is destroyed.")


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = None

    def create_bank_account(self, account_number, balance, account_type):
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        print(
            f"Customer '{self.name}' with bank account number {self.bank_account.account_number} is destroyed.")


customer1 = Customer("sadichhya maharjan", 23,"gwarko,lalitpur")
customer1.create_bank_account("5646456456", 40000, "Savings")

print(f"Customer Name: {customer1.name}")
print(f"Age: {customer1.age}")
print(f"Address: {customer1.address}")

print(f"Account Number: {customer1.bank_account.account_number}")
print(f"Balance: {customer1.bank_account.balance}")
print(f"Account Type: {customer1.bank_account.account_type}")

del customer1
