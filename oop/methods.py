class Student:
    clg_name = "gehu"
    print(clg_name)

    def __init__(self,fullname ):
        self.name = fullname
        
    def hello(self):
        print("hello ",self.name)

    def re(self):
        return self.name  
    
    

s1 = Student("Rahul")
s1.hello()

s2 = Student("arjun")
print("hello bhai ",s2.re())


















