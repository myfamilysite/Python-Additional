class Waiter:
    def __init__(self, name, table, gender):
        self.name = name
        self.table = table
        self.gender = gender
        
    def take_orders (self):
        return (f"{self.name} is taking orders on table {self.table}")
        
    def take_payments (self):
        return (f"{self.name} is handling payments on table {self.table}")
        

waiter1 = Waiter("Brian", 1, "male")
waiter2 = Waiter("Sindi", 2, "female")

print (waiter1.name)
print (waiter2.gender)

print (waiter1.take_orders())
print (waiter2.take_payments())




    
    