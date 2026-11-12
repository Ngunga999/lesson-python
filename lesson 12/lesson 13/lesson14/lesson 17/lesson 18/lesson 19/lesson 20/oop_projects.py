from bank_accounts import *

Ngunga = Bankaccount (1000, "Ngunga")
Sara = Bankaccount (2000, "Sara")

Ngunga.getbalance()
Sara.getbalance()

Sara.deposit(500)

Ngunga.withdraw(10000)

Ngunga.withdraw(1000)
Sara.withdraw(10)

Ngunga.transfer(10000, Sara)
Ngunga.transfer(100, Sara)

Jim = InterestRewardAcct(1000,"Jim")

Jim.getbalance()

Jim.deposit(100)

Jim.transfer(100,Ngunga)

Blaze = SavingsAcc(1000, "Blaze")

Blaze.getbalance()

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)