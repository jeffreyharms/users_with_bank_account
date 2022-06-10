class BankAccount:
    
    # Class parameters
    list_accounts = []
    bank_name = "Bank of the Weast"
    
    # Constructor method
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.list_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        self.balance -= amount
        if self.overdrawn(self.balance, amount):
            print("Insufficient funds!")
        return self
    
    def display_account_info(self):
        print("Balance: $", self.balance)
        
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return(self)
        
    @staticmethod
    def overdrawn(balance, amount):
        if balance - amount < 0:
            return False
        else:
            return True
        
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
    @classmethod
    def all_balances(cls):
        sum = 0
        for object in cls.list_accounts:
            sum += object.balance
        return sum 
    
class User:
    list_users = []
    # Constructor method
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account = BankAccount(0.03, 150)
        self.Savings = BankAccount(0.09, 1000)
        User.list_users.append(self)
        
    def display_user_balance(self):
        print("Name: ", self.name)
        print("email: ", self.email_address)
        print("Bank: ", self.account.bank_name)
        print("Checking Balance: $", self.account.balance)
        print("Checking Interest: %", self.account.int_rate)
        print("Savings Balance: $", self.Savings.balance)
        print("Savings Interest: %", self.Savings.int_rate)
        
    @classmethod
    def all_users(cls):
        for object in cls.list_users:
            print(object)
            
Hilde = User("Hilde", "hild@antisocial.com")
Gaston = User("Gaston", "noonefightslikegaston@neckbelts.com")

Gaston.account.change_bank_name("ECorp FCU")

Gaston.account.deposit(500)
Gaston.Savings.deposit(250)

Gaston.display_user_balance()
