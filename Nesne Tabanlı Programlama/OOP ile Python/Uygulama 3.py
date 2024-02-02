import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def showposition(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def disk(self, pt):  # İki nokta arasındaki uzaklık
        dx = pt.x - self.x
        dy = pt.y - self.y  # Self = p1 pt = p2
        return math.sqrt(dx ** 2 + dy ** 2)


p1 = Point(2, 3)
p2 = Point(3, 3)
print(p1.showposition())
print(p2.showposition())
p1.move(10, -10)
print(p1.showposition())
print(p2.showposition())
print(p1.disk(p2))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Person Name: ", self.name)
        print("Person Age = ", self.age)


P = Person("Thomas Wild", 37)
P.display()


class Sayi:
    def __init__(self, deger):
        self.deger = deger

    def ArmstrongtMu(self):
        ustoplamlari = 0
        for basamak in str(self.deger):
            ustoplamlari += int(basamak) ** len(str(self.deger))
        if self.deger == ustoplamlari:
            print("Şu sayı Armstrong sayısıdır: ", self.deger)
        else:
            print("Şu sayı Armstrong sayısı değildir: ", self.deger)


sayi1 = Sayi(371)
sayi2 = Sayi(657)
sayi1.ArmstrongtMu()
sayi2.ArmstrongtMu()