class bank:
    def __init__(self, number, name, balance):
        self.number=number
        self.balance=balance
        self.name=name
        #account owner name
    def deposit(self):
        add=input("Choose balance to deposit: ")
        self.balance=self.balance+int(add)
        print("New balance: " + str(self.balance))
    def withdrawl(self):
        subtract=input("Choose amount to withdrawl: ")
        if int(subtract)>self.balance:
            print("Not enough balance in account")
        if self.balance<-200:
            print("You ruined your life.")
        else:
            self.balance=self.balance-int(subtract)
            print("New balance: " + str(self.balance))

    def checkbal(self):
        print("Current balance: " + str(self.balance))

class locked(bank):
    def __init__(self, number, name, balance, isLocked):
        super().__init__(number, name, balance)
        self.isLocked=isLocked
    def locked(self):
        print("\n Your account is locked, use another account. \n")

class savings(bank):
    def __init__(self, number, name, balance):
        super().__init__(number, name, balance)
class checking(bank):
    def __init__(self, number, name, balance, isLocked):
            super().__init__(number, name, balance)

acct1=checking("0", "John", 203)
acct2=savings("1", "Olivia", 20)
acct3=checking("2", "Noah", 0)
acct4=savings("3", "Liam", -2000000)
acct5=locked("4", "Name5", 1002, True)
available=True
while True:
    if available:
        instruction=input("Input instruction: " + "\n" + "Options:"+ "\n withdrawl"+ " \n deposit" + "\n checkbal \n")
        available=False

    if instruction=="deposit":
        act=input("Input account number")
        if int(act)==0:
            acct1.deposit()
        if int(act)==1:
            acct2.deposit()
        if int(act)==2:
            acct3.deposit()
        if int(act)==3:
            acct4.deposit()
        if int(act)==4:
            acct5.locked()
        elif int(act)!=0 | int(act)!=1 | int(act)!=2 | int(act)!=3 | int(act)!=4:
            print("Account not found")
        instruction=""
        available=True


    if instruction=="withdrawl":
        act=input("Input account number")
        if int(act)==0:
            acct1.withdrawl()
        if int(act)==1:
            acct2.withdrawl()
        if int(act)==2:
            acct3.withdrawl()
        if int(act)==3:
            acct4.withdrawl()
        if int(act)==4:
            acct5.locked()
        elif int(act)!=0 | int(act)!=1 | int(act)!=2 | int(act)!=3 | int(act)!=4:
            print("Account not found")
        instruction=""
        available=True


    if instruction=="checkbal":
        act=input("Input account number")
        if int(act)==0:
            acct1.checkbal()
        if int(act)==1:
            acct2.checkbal()
        if int(act)==2:
            acct3.checkbal()
        if int(act)==3:
            acct4.checkbal()
        if int(act)==4:
            acct5.locked()
        elif int(act)!=0 | int(act)!=1 | int(act)!=2 | int(act)!=3 | int(act)!=3:
            print("Account not found")
        instruction=""
        available=True
    if instruction != "checkbal" or instruction!="deposit" or instruction!= "withdrawl":
        print("Not a valid instruction")
        instruction=""
        available=True
