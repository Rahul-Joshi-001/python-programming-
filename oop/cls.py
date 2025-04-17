class perosn:
    name = "anyonymous"

    @classmethod
    def changename(cls,name):
        cls.name = name


p1 = perosn();
print(p1.name)
p1.changename("rahul joshi")
print(p1.name)
