class bankaccount:
    def __init__(self):
        self.__balance = 0
    def get_balance(self):
        return self.__balance
    def set_deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print("successfully deposited")
        else:
            print("error")
account = bankaccount()
account.set_deposit(500)
account.set_deposit(-100)
print("balance:",account.get_balance())
