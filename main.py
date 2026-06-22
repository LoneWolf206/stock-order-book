from order_book import OrderBook
from portfolio import Portfolio

def print_book(book):
    state = book.get_order_book_state()
    print("\n--- ORDER BOOK ---")
    print("SELLS (lowest first):")
    for price, qty in state['sells']:
        print(f"  {price} x {qty}")
    print("BUYS (highest first):")
    for price, qty in state['buys']:
        print(f"  {price} x {qty}")
    print("------------------\n")

def main():
    book = OrderBook()
    alice = Portfolio("Alice")
    bob = Portfolio("Bob")
    bob.holdings = 50
    bob.avg_buy_price = 90  # Bob bought earlier at 90

    print("Stock Order Book Matching Engine")
    print("=" * 40)

    print("\nBob places a SELL order: 50 shares @ 100")
    book.add_order('sell', 100, 50)
    print_book(book)

    print("Alice places a BUY order: 30 shares @ 100")
    book.add_order('buy', 100, 30)
    print_book(book)

    print("Trades executed so far:")
    for t in book.trades:
        print(f"  Buy#{t['buy_id']} matched Sell#{t['sell_id']} "
              f"@ {t['price']} x {t['quantity']}")
        alice.record_buy(t['price'], t['quantity'])
        pnl = bob.record_sell(t['price'], t['quantity'])
        if pnl is not False:
            print(f"    Bob realized P&L: {pnl:.2f}")

    print(f"\n{alice}")
    print(f"{bob}")

    print("\nAlice places another BUY: 40 shares @ 105 (crosses spread)")
    book.add_order('buy', 105, 40)
    print_book(book)

    print("All trades:")
    for t in book.trades:
        print(f"  Buy#{t['buy_id']} matched Sell#{t['sell_id']} @ {t['price']} x {t['quantity']}")

if __name__ == "__main__":
    main()