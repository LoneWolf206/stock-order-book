class Portfolio:
    def __init__(self, name, cash=100000):
        self.name = name
        self.cash = cash
        self.holdings = 0          # number of shares held
        self.avg_buy_price = 0

    def record_buy(self, price, quantity):
        total_cost = price * quantity
        if total_cost > self.cash:
            print(f"{self.name}: insufficient cash for this buy")
            return False
        # update weighted average buy price
        total_shares = self.holdings + quantity
        self.avg_buy_price = (
            (self.avg_buy_price * self.holdings) + (price * quantity)
        ) / total_shares
        self.holdings = total_shares
        self.cash -= total_cost
        return True

    def record_sell(self, price, quantity):
        if quantity > self.holdings:
            print(f"{self.name}: insufficient holdings to sell")
            return False
        realized_pnl = (price - self.avg_buy_price) * quantity
        self.holdings -= quantity
        self.cash += price * quantity
        return realized_pnl

    def unrealized_pnl(self, current_price):
        return (current_price - self.avg_buy_price) * self.holdings

    def __repr__(self):
        return f"{self.name}: cash={self.cash:.2f}, holdings={self.holdings}, avg_buy={self.avg_buy_price:.2f}"