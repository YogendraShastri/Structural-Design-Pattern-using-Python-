# Subsystem 1
class PlaceOrder:
    def place_order(self, order):
        print(f"Customer Placed the Order for : {order}")

# Subsystem 2
class PrepareFood:
    def prepare_food(self, order):
        print(f"{order} is being prepared")

# Subsystem 3
class ServeOrder:
    def serve_order(self, order):
        print(f"{order} Prepared, Order Served")

# Facade:
class Waiter:
    def __init__(self):
        self.po = PlaceOrder()
        self.pf = PrepareFood()
        self.so = ServeOrder()

    def waiter_takeorder(self, order):
        self.po.place_order(order)
        self.pf.prepare_food(order)
        self.so.serve_order(order)


if __name__ == "__main__":
    cust1 = Waiter()
    cust1.waiter_takeorder("Pasta")
    



