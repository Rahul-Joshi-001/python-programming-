class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

    
class toyota(car):
    def __init__(self,name):
        self.name = name


caar = toyota("green")
car2 = toyota("brown")

print(caar.name)
print(caar.start( ))

