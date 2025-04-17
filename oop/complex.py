class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real,"i +",self.img," j")

    def __add__(self,num2):
        real = self.real + num2.real
        img = self.img + num2.real
        return complex(real,img)

    def 
num1 = complex(1,5)
num1.show()

num2 = complex(3,6)
num2.show()

print("addition of no is :- ")
num3  = num1 + num2
num3.show()