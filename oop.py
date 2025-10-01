class Registration():
    def __init__(self,name ,phone,address,balance):
        self.name=name
        self.phone=phone
        self.address=address
        self._balance=balance
        print(f"welcome {self.name} your balance is {self._balance}")
    
    def change_phone_number(self):
        self.phone=input("enter your phone +20 ")
        self.phone= "+20"+self.phone
    
    def display_info(self):
        print(f"NAME = {self.name} \nPHONE = {self.phone} \naddress = {self.address} \nBALANCE = {self._balance}  ")

class BankAccount(Registration):
    def __init__(self,name ,phone,address,balance):
        Registration.__init__(self,name ,phone,address,balance)

    def deposit(self,amount):
        self.amount=amount
        self._balance += self.amount
        return  self._balance
    
    def withdraw(self,amount) :
        self.amount=amount
        if self.amount <=self._balance:
            self._balance -= self.amount
            return  self._balance
        else:
            return "your current balance doesnot enough"
    
    def getbalance(self):
        return self._balance
    
    # def setbalance (self, balance):
    #     self.balance=balance
    #     self.__balance=balance
    #     return self.__balance
    
firstcusmor=BankAccount("Ahmed","5020101020","cairo",1000000)
# firstcusmor.change_phone_number()
firstcusmor.display_info()
print(firstcusmor.deposit(50000))
print(firstcusmor.withdraw(50000))