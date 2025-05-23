class VendingMachine:
    def __init__(self, num_items, price):
        self.num_items = num_items  # Total items in the machine
        self.price = price          # Price per item

    def display_info(self):
        print(f"Items available: {self.num_items}")
        print(f"Price per item: ${self.price}")

    def buy(self, quantity, money):
        total_cost = quantity * self.price

        if quantity > self.num_items:
            return("not enough items")

        if money < total_cost:
            return("Insufficient funds")

        self.num_items -= quantity
        change = money - total_cost
        print(f"Items remaining: {self.num_items}")
        return(f"Purchase successful. Change: ${change:.2f}")
