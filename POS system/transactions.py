class Stock(object):
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        self.product = []
    
    def add_product(self, product_name, amount):
        self.product.append((product_name, amount))  # ✅ Adds a new expense as a (name, amount) pair to the expenses list
    
    def reduce_stock(self):
        for name, amount in self.product:
            total -= amount
        return total
        
    def calculate_total(self):
        total = 0
        for name, amount in self.product:  #✅ Explanation:
            total += amount                    # Assumes each item in self.expenses is a tuple of two values, like ("Rent", 5000)
        return total                           # Unpacks it into name and amount
                                            # Adds only the amount part
                                            
    def display_summary(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print("New stock:")
        for name, amount in self.product:
            print(f"  {name}: {amount}")
        print(f"Total Amount: {self.calculate_total()}")
                                            
    # def display_info(self):
    #     print("Product name: ", self.name, "Product price: ", self.price, "Product total: ", self.total)