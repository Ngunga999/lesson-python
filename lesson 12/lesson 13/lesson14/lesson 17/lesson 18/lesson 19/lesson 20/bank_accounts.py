class BalanceException(Exception):
     pass


class Bankaccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getbalance(self):
        print(f"\nAccount '{self.name}' balance = $ {self.balance:.2f}")

    def deposit(self, amount):
            self.balance = self.balance + amount
            print("\nDeposit complete.")
            self.getbalance()
    def viableTransaction(self, amount):
         if self.balance >=amount: return

         else:
          raise BalanceException(f"\nSorry, account '{self.name}'only has a balance of $ {self.balance:.2f}")  


def withdraw (self, amount):
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nwithdraw complete")
            self.getbalance()
        except BalanceException as error:
            print(f'\nwithdraw interrupted: {error}')
            
def transfer(self, amount, account):
    try: 
        print('\n**********\n\nBeginning Transfer..🚀 ')
        self.viableTransaction(amount)
        self.withdraw(amount)
        account.depsit(amount)
        print('\nTransfer complete! ✅\n\n**********')
    except BalanceException as error:
        print(f'\nTransfer interrupted. ❌ {error}')

class InterestRewardAcct(Bankaccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount *  1.05)
        print("\nDeposit complete")
        self.getbalance()


class SavingsAcc(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5 

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance =self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getbalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')    

