# 4 - oy 12 dars
# dataclass
# homeworks
from dataclasses import dataclass

# 1.
@dataclass
class Product:
    name: str
    _price: float
    availability: bool

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Narx faqat ijobiy qiymat bo'lishi kerak.")

class ElectronicProduct(Product):
    def __init__(self, name, price, availability, warranty):
        super().__init__(name, price, availability)
        self.warranty = warranty

# 2.
@dataclass
class Vehicle:
    brand: str
    _speed: int

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value <= 300:
            self._speed = value
        else:
            raise ValueError("Tezlik 300 dan oshmasligi kerak.")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

class Bicycle(Vehicle):
    def __init__(self, brand, speed, brake_type):
        super().__init__(brand, speed)
        self.brake_type = brake_type

# 3.
@dataclass
class Book:
    title: str
    author: str
    _price: float

    def set_price(self, value, is_admin):
        if is_admin:
            self._price = value
        else:
            raise PermissionError("Faqat admin narxni o'zgartirishi mumkin.")

class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

class PrintedBook(Book):
    def __init__(self, title, author, price, paper_type):
        super().__init__(title, author, price)
        self.paper_type = paper_type

# 4.
@dataclass
class Employee:
    name: str
    position: str
    _salary: float

    def increase_salary(self, amount, is_director):
        if is_director:
            self._salary += amount
        else:
            raise PermissionError("Faqat direktor maoshni oshirishi mumkin.")

class Manager(Employee):
    def manage_team(self):
        return f"{self.name} jamoani boshqaradi."

class Developer(Employee):
    def write_code(self):
        return f"{self.name} kod yozmoqda."

# 5.
@dataclass
class Athlete:
    name: str
    sport_type: str
    _records: list

    def update_record(self, new_record):
        self._records.append(new_record)

class Runner(Athlete):
    def __init__(self, name, sport_type, records, distance):
        super().__init__(name, sport_type, records)
        self.distance = distance

    def run(self):
        return f"{self.name} {self.distance} km masofani yugurmoqda."

class Swimmer(Athlete):
    def __init__(self, name, sport_type, records, pool_length):
        super().__init__(name, sport_type, records)
        self.pool_length = pool_length

    def swim(self):
        return f"{self.name} {self.pool_length} metrlik havzada suzmoqda."


