class bank:
    def __init__(self,balance,acc):
        self.balance = balance
        self.acc = acc

    def debit(self,amount):
        self.balance -= amount
        print("RS",amount,"was debited from your bank account no",self.acc)

    def credit(self,amount):
            self.balance += amount
            print("RS",amount,"is add to your account")

    def check_bal(self):
            print("your current balance is : ",self.balance)


acc1= bank(2000,12345)

acc1.debit(1000)
acc1.check_bal()


acc1.credit(5000)
acc1.check_bal()

del acc1;
