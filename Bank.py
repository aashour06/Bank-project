import DataBase

class Registration():
    def __init__(self,name ,phone,address,balance,password):
        self.name=name
        self.phone=phone
        self.address=address
        self.balance=balance
        self.password=password
        
        DataBase.addToDataBase(name ,phone,address,balance,password)
        print(f"welcome {self.name} your balance is {self.balance}")
    
    def change_phone_number(self,name,password):
        DataBase.change_phone(name,password)
        

    
    def display_info(self,name,password):
        DataBase.display_info_from_db(name,password)

class BankAccount(Registration):
    def __init__(self,name ,phone,address,balance,password):
        Registration.__init__(self,name ,phone,address,balance,password)

    def deposit(self,name,password,amount):
        DataBase.deposite(name,password,amount)
    
    def withdraw(self,name,password,amount) :
        DataBase.withdraw(name,password,amount)


    
# firstcusmor=BankAccount("Ahmed","5020101020","cairo",1000000,1234)
# firstcusmor.change_phone_number("Ahmed",1234)
# firstcusmor.deposit("Ahmed",1234,50000)
# firstcusmor.withdraw("Ahmed",1234,100000)
sec=BankAccount("Austin Lucas","55151","sskdmcksd",115151551,9000)