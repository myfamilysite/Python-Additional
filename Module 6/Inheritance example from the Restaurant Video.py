class Staff:
    def __init__(self, name, shift):
        self.name = name
        self.shift = shift
        
    def start_work(self):
        print(f"{self.name} starts work on {self.shift} shift")
        
class Waiter(Staff):
    def take_order(self):
        print(f"{self.name} is taking an order")
        
class Chef(Staff):
    def cook_food(self):
        print (f"{self.name} is cooking food.")
        
raj = Waiter("Raj", "Morning")
amit = Chef("Amit", "Night")

raj.take_order()
amit.cook_food()

raj.start_work()
amit.start_work()

