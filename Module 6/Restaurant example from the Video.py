class Waiter:
    def __init__(self):
        self.tables = []
        
    def take_order(self):
        print("Order taken")
        
Raj = Waiter()
Simran = Waiter()

Raj.take_order()
Simran.take_order()

Raj.tables.append([4,5,6])
print(Raj.tables)

Simran.tables.append([1,2,3])
print(Simran.tables)