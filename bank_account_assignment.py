class BankAccount:
    Rate = 0
    Bal = 0
    
    def __init__(self, int_rate, balance): 
        self.Rate = int_rate
        self.Bal = balance
        
    def deposit(self, amount):
        self.Bal = self.Bal + amount
    def withdraw(self, amount): 
        self.Bal = self.Bal - amount
    def display_account_info(self):
        print(self.Bal)
    def yield_interest(self):
        print(self.Rate)

Roche = BankAccount(27,8000)
Nico = BankAccount(14,6812864)

Roche.deposit(1000)
Roche.deposit(600)
Roche.deposit(700)
Nico.withdraw(1468500)
Nico.display_account_info()
Roche.withdraw(800)
Nico.deposit(16000)
Nico.deposit(14538)
Roche.display_account_info()
Nico.yield_interest()