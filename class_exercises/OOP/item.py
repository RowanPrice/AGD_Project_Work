class Item:
    # Constructor
    def __init__(self, name, description, price, stock: int = 100):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock