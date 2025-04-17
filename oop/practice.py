class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order):
        return self.price > order.price


o1 = order("pop",50)
o2 = order("tea",30)

print(o1>o2);

