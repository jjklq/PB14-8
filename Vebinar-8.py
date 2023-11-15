class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def view_students(self):
        for student in self.students:
            print(student.name)

    def view_courses(self):
        for course in self.courses:
            print(course.name)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)

    def view_courses(self):
        for course in self.enrolled_courses:
            print(course.name)

class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code

# Example of usage
uni = University("Harvard")

maths = Course("Mathematics", "MATH101")
physics = Course("Physics", "PHYS101")

uni.add_course(maths)
uni.add_course(physics)

alice = Student("Alice", "S101")

uni.add_student(alice)

alice.enroll(maths)

alice.view_courses()  # Output: Mathematics

uni.view_students()  # Output: Alice
uni.view_courses()  # Output: Mathematics



class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Warehouse:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = quantity

    def view_stock(self):
        for product, quantity in self.products.items():
            print(f"{product.name}: {quantity}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_item(product, quantity)

    def view_cart(self):
        return self.shopping_cart.view_items()

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def view_items(self):
        return self.items

class Order:
    def __init__(self, user, warehouse):
        self.user = user
        self.warehouse = warehouse

    def place_order(self):
        for product, quantity in self.user.shopping_cart.items.items():
            if product in self.warehouse.products and quantity <= self.warehouse.products[product]:
                self.warehouse.products[product] -= quantity
            else:
                print(f"Product {product.name} is not available in sufficient quantity.")
        self.user.shopping_cart.items = {}  # Clear the shopping cart

# Example of usage
warehouse = Warehouse()
apple = Product("Apple", "Fresh Red Apple", 0.5)
banana = Product("Banana", "Fresh Yellow Banana", 0.3)

warehouse.add_product(apple, 100)
warehouse.add_product(banana, 150)

user = User("John Doe", "john.doe@example.com")

user.add_to_cart(apple, 5)
user.add_to_cart(banana, 10)

print(user.view_cart())  # Output: {'Apple': 5, 'Banana': 10}

order = Order(user, warehouse)
order.place_order()

print(user.view_cart())  # Output: {}
print(warehouse.view_stock())  # Output: Apple: 95, Banana: 140
