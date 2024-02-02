# Single Inheritance

# Parent Class
class Person:
    def person_info(self):
        print("Person sınıfında")


# Child Class
class Student(Person):
    def student_info(self):
        print("Student sınıfında")


student = Student()

student.student_info()
student.person_info()


# Multiple Inheritance

# Parent Class
class Person:
    def person_info(self):
        print("Person sınıfında")


# Parent Class
class School:
    def school_info(self):
        print("School sınıfında")


# Child Class
class Student(Person, School):
    def student_info(self):
        print("Student sınıfında")


student = Student()

student.student_info()
student.school_info()
student.person_info()


# Multilevel Inheritance

class Vehicle:
    def vehicle_info(self):
        print("Vehicle Sınıfda")


class Car(Vehicle):
    def car_info(self):
        print("Car Sınıfında")


class SportsCar(Car):
    def sportsCar_info(self):
        print("SporsCar Sınıfda")


sportsCar = SportsCar

sportsCar.sportsCar_info()
sportsCar.car_info()
sportsCar.vehicle_info()


# Hierarchical Ingeritance

# Parent Class

class Vehicle:
    def vehicle_info(self):
        print("Vehicle Sınıfda")


# Child Class
class Car(Vehicle):
    def car_info(self):
        print("Car Sınıfında")


# Child Class

class Truck(Vehicle):
    def truck_info(self):
        print("Truck Sınıfında")


car = Car()
car.car_info()
car.vehicle_info()

truck = Truck()
truck.truck_info()
truck.vehicle_info()


# Hybrid Inheritance

# Parent Class

class Vehicle:
    def vehicle_info(self):
        print("Vehicle Sınıfda")


# Child Class
class Car(Vehicle):
    def car_info(self):
        print("Car Sınıfında")


# Child Class

class Truck(Vehicle):
    def truck_info(self):
        print("Truck Sınıfında")


class Ozellik:
    def ozellik_info(self):
        print("Özellik Sınıfında")


class SportsCar(Car, Ozellik):
    def sportsCar_info(self):
        print("SporsCar Sınınfda")
