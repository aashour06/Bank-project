class BankAccount():
    def __init__(self,balance):
        self.balance=balance
        self.__balance=balance
        print(f"Hello custmore your balance is {self.balance}")
    
    def deposit(self,amount):
        self.amount=amount
        self.__balance += self.amount
        return  self.__balance
    
    def withdraw(self,amount) :
        self.amount=amount
        if self.amount <=self.__balance:
            self.__balance -= self.amount
            return  self.__balance
        else:
            return "your current balance doesnot enough"
    
    def getbalance(self):
        return self.__balance
    
    # def setbalance (self, balance):
    #     self.balance=balance
    #     self.__balance=balance
    #     return self.__balance
    
c1=BankAccount(50000)
print(c1.deposit(10000))
print(c1.withdraw(5000))
# print(c1.setbalance(1000000))
print(c1.withdraw(100000000))