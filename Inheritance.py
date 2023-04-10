class Parent:
    def __init__(self):
        print("Class parent init method")
    def config1(self):
        print("Parent class - Config1 method")

    def config2(self):
        print("Parent class - Config2 method")


class Child(Parent):
    def __init__(self):
        print("Class Child INIT method")
    def config3(self):
        print("Child class - Config3 method")

    def config4(self):
        print("Child class - Config4 method")
class GrandChild(Child):
    def config5(self):
        super().__init__()
        print("Class GrandChild - Method config5")



#ch1 = Child();
#ch1.config1()

gc1 = GrandChild()
gc1.config5()
