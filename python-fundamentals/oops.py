# BASIC CLASS AND OBJECT 
# Problem -> Create a class Car with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Car Brand: {self.brand}, Model: {self.model}"
    
my_car = Car("Toyota", "Corolla")
print(my_car.display())

# Output:
# Car Brand: Toyota, Model: Corolla

# ------------------------------------------------------------------------------------------------------------------

# INHERITANCE
# Problem -> Create an ElectricCar class that inherits from the Car class and adds an additional attribute for battery capacity.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Car Brand: {self.brand}, Model: {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_Electric_Car = ElectricCar("Tesla", "X", "85Kwh")
print(my_Electric_Car.battery_size)
print(my_Electric_Car.display())

# Output:
# 85Kwh
# Car Brand: Tesla, Model: X

# ------------------------------------------------------------------------------------------------------------------

# ENCAPSULATION
# Problem -> Modify the Car class to encapsulate the brand attribute, making it private and providing a getter method to access it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"
    
    def display(self):
        return f"Car brand: {self.__brand}, Model: {self.model}"
    
my_car = Car("Tesla", "X")
print(my_car.display())     # Car brand: Tesla, Model: X
print(my_car.get_brand())   # Tesla!
# print(my_car.__brand)     # ❌ This will raise an AttributeError since __brand is private

# ------------------------------------------------------------------------------------------------------------------

# POLYMORPHISM
# Problem -> Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes but with different behaviours.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"
    
my_car = Car("Toyota", "Corolla")
my_electric_car = ElectricCar("Tesla", "Model S", "100kWh")
print(my_car.fuel_type())
print(my_electric_car.fuel_type())

# Output:
# Petrol or Diesel
# Electric

# ------------------------------------------------------------------------------------------------------------------

# STATIC METHODS
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y

calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(10, 4))

# Output:
# 8
# 6

# ------------------------------------------------------------------------------------------------------------------

# PROPERTY DECORATORS
class Student:
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

s = Student("Rishabh")
print(s.name)
s.name = "Rishabh Raj"
print(s.name)
# s.__name = "Rishabh Raj"  # ❌ This will not change the name as __name is private

# Output:
# Rishabh
# Rishabh Raj

# ------------------------------------------------------------------------------------------------------------------

# CLASS INHERITANCE AND isinstance()
class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def speak(self):
        return "Dog barks"
    
class Cat(Animal):
    def speak(self):
        return "Cat meows"

dog = Dog()
cat = Cat()
print(isinstance(dog, Animal))  
print(isinstance(cat, Animal))  
print(isinstance(dog, Dog))     
print(isinstance(cat, Dog))     
print(isinstance(cat, Cat))     

# Output:
# True
# True
# True
# False
# True

# ------------------------------------------------------------------------------------------------------------------

# MULTIPLE INHERITANCE 
class Battery:
    def info(self):
        return "This is a battery"

class Engine:
    def info(self):
        return "This is an engine"

class ElectricCar(Battery, Engine):
    pass
    
my_electric_car = ElectricCar()

print(my_electric_car.info())           # MRO -> Takes Battery's info() first
print(Battery.info(my_electric_car))    # Calling Battery explicitly
print(Engine().info())                  # Engine info

# Output:
# This is a battery
# This is a battery
# This is an engine
