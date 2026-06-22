import heapq
from order import Order

class OrderBook:
    def __init__(self):
        self.buy_heap = []   # max-heap: store as (-price, timestamp, order)
        self.sell_heap = []  # min-heap: store as (price, timestamp, order)
        self.trades = []

    def add_order(self, side, price, quantity):
        order = Order(side, price, quantity)

        if side == 'buy':
            heapq.heappush(self.buy_heap, (-price, order.id, order))
        else:
            heapq.heappush(self.sell_heap, (price, order.id, order))

        self.match_orders()
        return order

    def match_orders(self):
        while self.buy_heap and self.sell_heap:
            best_buy_price = -self.buy_heap[0][0]
            best_sell_price = self.sell_heap[0][0]

            if best_buy_price < best_sell_price:
                break  # no match possible

            buy_order = self.buy_heap[0][2]
            sell_order = self.sell_heap[0][2]

            trade_qty = min(buy_order.quantity, sell_order.quantity)
            trade_price = sell_order.price  # convention: trade at resting order's price

            self.trades.append({
                'buy_id': buy_order.id,
                'sell_id': sell_order.id,
                'price': trade_price,
                'quantity': trade_qty
            })

            buy_order.quantity -= trade_qty
            sell_order.quantity -= trade_qty

            if buy_order.quantity == 0:
                heapq.heappop(self.buy_heap)
            if sell_order.quantity == 0:
                heapq.heappop(self.sell_heap)

    def get_order_book_state(self):
        buys = sorted([(-p, o.quantity) for p, _, o in self.buy_heap], reverse=True)
        sells = sorted([(p, o.quantity) for p, _, o in self.sell_heap])
        return {'buys': buys, 'sells': sells}