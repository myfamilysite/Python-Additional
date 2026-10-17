class Waiter:
    def __init__(self, name, tables, attitude):
        self._name = name
        self._tables = tables
        self._attitude = attitude
        
    def orders (self):
        print (f"{self._name} is taking orders on tables {self_.tables}")
        
    def payments (self):
        print (f"{self._name} is handling payments on tables {self._tables}")
        

waiter1 = Waiter("Brian", [4,5], "friendly")
waiter2 = Waiter("Joe",[1,2,7], "grumpy")

(waiter1.orders())

(waiter2.attitude)

(waiter2.payments())
    
    