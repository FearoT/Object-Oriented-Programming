class A:
    def __init__(self, num):
        num = 3
        self.num = num

    def change(self):
        self.num = 7


a = A(5)
print(a.num)
a.change()
print(a.num)
print("-------------------------------------")


class B:
    def __init__(self, count=100):
        self.count = count


obj1 = B()
obj2 = B(102)
print(obj1.count)
print(obj2.count)
print("-------------------------------------")


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(self.id)


std = Student("Simon", 1)
std.id = 2
print(std.id)