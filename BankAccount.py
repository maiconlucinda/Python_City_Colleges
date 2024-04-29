
# PART 1

class BankAccount:

    def __init__(self, account_holder, pin, balance=0):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.overdraft_status = self.set_overdraft_status()



    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        self.overdraft_status = self.set_overdraft_status()



    def withdraw(self, amount):
        # If we use this logic commented we would never have negative balance, becuase the amount will not get below zero.
        #if amount > 0 and amount < self.balance:
        if amount > 0:
            self.balance -= amount
        self.overdraft_status = self.set_overdraft_status()   
        
            
        


    def set_overdraft_status(self):
        if self.balance < 0:
            return True
        else:
            return False
        

