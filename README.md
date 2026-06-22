# Stock Order Book Matching Engine

A limit order book matching engine implementing price-time priority, built with dual heap data structures, with portfolio and P&L tracking.

## How It Works

**Dual Heap Architecture:**
- Buy orders stored in a max-heap (highest price matched first)
- Sell orders stored in a min-heap (lowest price matched first)
- Python's heapq is min-heap only, so buy prices are negated to simulate a max-heap

**Price-Time Priority:**
- Orders at the same price are matched in the order they arrived (FIFO)
- Each order gets a unique auto-incrementing ID for tie-breaking in the heap

**Matching Logic:**
- A trade executes whenever the best buy price >= best sell price
- Partial fills are supported — an order can be matched against multiple counter-orders
- Trade price follows the resting order's price (price improvement for the aggressor)

**Portfolio Tracking:**
- Weighted average buy price calculated per trader
- Realized P&L computed on every sell
- Unrealized P&L computable against current market price

## Complexity
- Insert order: O(log n)
- Match best buy/sell: O(1) lookup, O(log n) removal
- Overall: O(log n) per order — same as any heap-based priority queue

## Stack
Python · heapq

## Run
python main.py

## Sample Output
Demonstrates a sell order being partially filled by two separate buy orders, with portfolio cash, holdings, and realized P&L updating correctly after each trade.

## Architecture
- `order.py` — Order object with auto-incrementing ID
- `order_book.py` — Heap-based matching engine
- `portfolio.py` — Cash, holdings, and P&L tracking per trader
- `main.py` — CLI demo simulating a trading session
