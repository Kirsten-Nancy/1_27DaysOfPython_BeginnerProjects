class Parent:
    def __init__(self):
        self.name = 'parent'

    def print_name(self):
        print(f" from parent: My name is {self.name}")


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = 'Child'

    def print_name(self):
        super().print_name()
        # self.name = 'Child'
        # print(self.name)



child1 = Child()
child1.print_name()
