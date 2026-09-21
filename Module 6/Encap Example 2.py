class Restaurant:
    def __init__(self, table, food):
        self.table = table
        self.food = food
        
    def serve(self, table, food):
         print(f"The waiter is serving table {table} {food}")
         
    def cook(self, table, food):
         print(f"The cook is cooking {food} for table {table} ")
        
        
waiter1 = Restaurant(1, "stew")

chef1 = Restaurant(2, "curry")

waiter1.serve(1, "stew")

chef1.cook(2, "curry")


