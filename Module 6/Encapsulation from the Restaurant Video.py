class Waiter:
    def __init__(self):
        self.tables = []
        
    def take_order(self):
        print("Order taken")
        
    def add_table(self, table_number):
        self.tables.append(table_number)
        
Raj = Waiter()
Simran = Waiter()

Raj.add_table(4)
Raj.add_table(5)
print(Raj.tables)

Simran.add_table(1)
print(Simran.tables)
