class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
        
        # your code here
    def withdraw(self, amount):
        if(self.balance - amount >= 0):
            self.balance -= amount
        else:
            print("Insufficient funds: Charing a $5 fee")
            self.balance -= 5
        print(self.balance)
        return self
        # your code here
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate} - Balance: {self.balance}")
        return self
        # your code here
    def yield_interest(self):
        self.balance = self.balance * (1 + self.int_rate)
        print(self.balance)
        return self
        # your code here

# account1 = BankAccount(.02,100)
# account2 = BankAccount(.03,500)

# account1.display_account_info()

# account1.deposit(50).deposit(25).deposit(100).withdraw(75).yield_interest().display_account_info()
# account2.deposit(100).deposit(50).withdraw(25).withdraw(25).withdraw(75).withdraw(50).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
    	self.account.deposit(amount)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        # self.account.display_account_info()
        print(self.account.balance)

user1 = User("Bob", "bob@email.com")

user1.make_deposit(20)
user1.make_withdrawal(10)
user1.display_user_balance()