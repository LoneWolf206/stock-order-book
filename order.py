import itertools

class Order:
    _id_counter = itertools.count(1)

    def __init__(self, side, price, quantity):
        self.id = next(Order._id_counter)
        self.side = side          # 'buy' or 'sell'
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Order(id={self.id}, {self.side}, price={self.price}, qty={self.quantity})"