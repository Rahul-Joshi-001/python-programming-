class account:
    def __init__(self,acc_no,acc_pass):
         self.acc_no = acc_no
         self.__acc_pass = acc_pass

    def print_pass(self):
         print("your password is : ",self.__acc_pass)


ac1 = account("12345","rahul123")
print(ac1.acc_no)
ac1.print_pass()