class Footballer:
    football_club = "Barcelona"
    age = 30


f1 = Footballer()
print(f1)
print(f1.age)
print(f1.football_club)
f1.football_club = "Real Madrid"


class Square(object):
    edge = 4
    area = 0

    def area(self):
        self.area = self.edge * self.edge
        print("Area:", self.area)

    pass


s1 = Square()
print(s1.area())


class employye(object):
    age = 25
    salary = 1000

    def ageSalaryRatio(self):
        a = self.age / self.salary
        return a


e1 = employye()


def ageSalaryRatio(a, b):
    area = a * b ** 2
    print("Function=", area)


func = e1.ageSalaryRatio()
print("ss", func)
ageSalaryRatio(50, 20000)


class Animal(object):
    def __init__(self, a, b):
        self.name = a
        self.age = b

    def getAge(self):
        return self.age


animal1 = Animal("dog", 2)
animal2 = Animal("cat", 3)
animal3 = Animal("bird", 4)
print("dog", animal1.age, animal1.name)
yas = animal1.getAge()
print("yas", yas)
