class Staff:
    def __init__(self, name, shift):
        self.name = name
        self.shift = shift
        
    def start_work(self):
        print(f"{self.name} starts work on {self.shift} shift")
        
    def work(self):
        print(f"{self.name} is working")
        
class Waiter(Staff):
    def take_order(self):
        print(f"{self.name} is taking an order")
        
    def work(self):
        self.take_order()
        
class Chef(Staff):
    def cook_food(self):
        print (f"{self.name} is cooking food.")
        
    def work(self):
        self.cook_food()
        
raj = Waiter("Raj", "Morning")
amit = Chef("Amit", "Night")

raj.work()
amit.work()

